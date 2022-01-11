from pyEarnapp import EarnApp

IPsToCheck = [
    '192.168.0.1',
    '192.168.0.2',
    # And so on...
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


api = EarnApp('')
for ip in IPsToCheck:
    print(api.is_ip_allowed(ip, proxies=format_request_proxy(proxy)))
    i += 1
    proxy = proxies[i % len(proxies)]
