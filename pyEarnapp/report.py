from urllib import parse
from requests import get
from urllib.parse import urljoin

def report_banned_ip(ipaddress:str):
    try:
        url = urljoin('https://ipban.ffehost.com/ban/', ipaddress)
        get(url)
    except:
        parse