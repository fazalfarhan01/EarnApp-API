from pyEarnapp import EarnApp

AUTHS = [

]

proxies = [
# "proxy_ip:proxy_port:username:passowrd"
]
i = 0
proxy = proxies[i]


def format_request_proxy(proxy: str):
    proxy = proxy.split(':')
    url = f'socks5://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'
    return {
        'http': url,
        'https': url,
    }


tx_info = {
    'approved':0,
    'paid':0,
    'created':0,
    'pending_procedure':0,
    'not_paid':0
}


for auth in AUTHS:
    api = EarnApp(auth)
    
    transaction_info = api.get_transaction_info(proxies = format_request_proxy(proxy))
    for transaction in transaction_info.transactions[:10]:
        if transaction.status in ['approved', 'pending_procedure']:
            tx_info[transaction.status] += transaction.amount
            print(f"Amount of {transaction.amount:6.2f} is {transaction.status} to {transaction.email}")

    i += 1
    proxy = proxies[i]

for key, value in tx_info.items():
    print(f"Status: {key:10s} Amount: {value}")
