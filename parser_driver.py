from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

from params import BROWSER_HOST, DO_WRITE_TO_FILE

import logging


def parse():
    target_url = 'https://kurs.kz/'

    logging.warning('pre browser')
    html = get_target_html(target_url)
    logging.warning('post browser')
    data = get_data(html)
    if DO_WRITE_TO_FILE:
        write_to_file(data)
    return data


def get_target_html(url, useragent=None, proxy=None):
    driver = webdriver.Remote(BROWSER_HOST, DesiredCapabilities.FIREFOX)
    # driver = webdriver.Firefox()
    logging.warning('get url')
    driver.get(url)
    html = driver.page_source
    driver.quit()
    # driver.close()
    return html


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    target_trs = soup.find('div', id='table').find('tbody').find_all('tr', class_=["punkt-close", "punkt-open"])

    data = []
    for tr in target_trs:
        tds = tr.find_all('td')
        name = tds[0].find('a').text.strip()
        address = tds[0].find('address').text.strip()

        usd_tags = tds[2].find_all('span')
        usd_buy = usd_tags[0].text.strip()
        usd_sale = usd_tags[2].text.strip()

        eur_tags = tds[3].find_all('span')
        eur_buy = eur_tags[0].text.strip()
        eur_sale = eur_tags[2].text.strip()

        rub_tags = tds[4].find_all('span')
        rub_buy = rub_tags[0].text.strip()
        rub_sale = rub_tags[2].text.strip()

        phones = [tag.text.strip() for tag in tds[5].find_all('a', class_='phone')]

        usd_data = make_data(name, address, phones[-1], 'USD', usd_buy, usd_sale)
        eur_data = make_data(name, address, phones[-1], 'EUR', eur_buy, eur_sale)
        rub_data = make_data(name, address, phones[-1], 'RUB', rub_buy, rub_sale)

        data.extend([usd_data, eur_data, rub_data])

    return data


def make_data(entity_name, entity_address, entity_phone, currency_name, buy, sale):
    return {
            'entity_name': entity_name,
            'entity_address': entity_address,
            'entity_phone': entity_phone,
            'currency_name': currency_name,
            'buy': buy,
            'sale': sale
        }


def write_to_file(data):
    with open("tmp.txt", "w") as txtfile:
        for line in data:
            txtfile.write(str(line))
