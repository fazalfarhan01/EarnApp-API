# THIS IS AN EXAMPLE CODE ON THE USAGE OF PROXY ALONG WITH THE EARNAPP API
# THIS CODE CALCULATES ALL THE CURRENT EARNINGS ON MULTIPLE ACCOUNTS
# IT DOES SO BY USING PROXIES TO AVOID BEING RATE LIMITED BY EARNAPP

from pyEarnapp import EarnApp
import pyEarnapp.errors as EAErrors
import threading

AUTHS = {
    'mine': [
        "Your Auth tokens"
    ]
}

proxies = [
    "proxy_ip:proxy_port:username:passowrd"
]

i = 0
proxy = proxies[i]


def format_request_proxy(proxy: list):
    proxy = proxy.split(':')
    url = f'socks5://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'
    return {
        'http': url,
        'https': url,
    }


def get_info(api):
    global proxy, i
    try:
        earning_info = api.get_earning_info(
            proxies=format_request_proxy(proxy))
        user_info = api.get_user_data(proxies=format_request_proxy(proxy))
        transaction_info = api.get_transaction_info(
            proxies=format_request_proxy(proxy))
        devices_info = api.get_devices_info(
            proxies=format_request_proxy(proxy))
        return earning_info, user_info, transaction_info, devices_info
    except EAErrors.TooManyRequestsError:
        print("[X] Rate limit triggered. Changing proxy.")
        i += 1
        proxy = proxies[i]
        return get_info()


today_total = {}
yesterday_total = {}
threads = []


def in_thread(api, person):
    global today_total, yesterday_total
    earning_info, user_info, transaction_info, device_info = get_info(api)
    try:
        transaction = transaction_info.transactions[0]
        amount = transaction.amount
        status = transaction.status
    except Exception as e:
        print(e)
        amount = 0
        status = None
    print(
        f'[!] ID: {user_info.email:30s} Balance: {earning_info.balance:6.2f}\tYesterday: {amount:6.2f} {status}')
    try:
        today_total[person] += earning_info.balance
        yesterday_total[person] += transaction_info.transactions[0].amount
    except:
        pass


for one_person_auths in AUTHS.keys():
    today_total[one_person_auths] = 0
    yesterday_total[one_person_auths] = 0
    for i in range(len(AUTHS[one_person_auths])):
        threads.append(threading.Thread(
            target=in_thread, args=[EarnApp(AUTHS[one_person_auths][i]), one_person_auths]))
        i += 1
        proxy = proxies[i]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for person in AUTHS.keys():
    print(f"[💵] {person.title():8s} | Today's earning: ${today_total[person]:6.2f} | Yesterday's earning: ${yesterday_total[person]:6.2f}")
