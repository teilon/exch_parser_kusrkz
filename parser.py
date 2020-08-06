import requests
from bs4 import BeautifulSoup

target_url = 'https://kurs.kz/'

def parse():
    html = get_target_html(target_url)
    get_data(html)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    prettyHTML = soup.prettify()
    # target_tags = soup.find('div', id='table').find('tbody').find_all('tr', class_="punkt-close")
    # target_tags = soup.find_all('tr', class_="punkt-close")
    target_tags = soup.find('div', id='table')

    with open('tmp0.txt', 'a') as f:
        f.write(prettyHTML)


def get_target_html(url, useragent=None, proxy=None):
    r = requests.get(url, headers=useragent, proxies=proxy, verify=False)
    return r.text