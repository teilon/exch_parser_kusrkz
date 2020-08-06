from selenium import webdriver
from bs4 import BeautifulSoup

def parse():
    target_url = 'https://kurs.kz/'

    html = get_target_html(target_url)
    get_data(html)

def get_data(html):
    # with open('tmp.txt', 'a') as f:
    #     f.write(html)

    soup = BeautifulSoup(html, 'lxml')
    target_trs = soup.find('div', id='table').find('tbody').find_all('tr', class_=["punkt-close", "punkt-open"])

    n = 0;
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

        # bank_data = {
        #     'handler_name': bank_name,
        #     'money_type': money_type,
        #     'name': currency_name,
        #     'buy': buy,
        #     'sale': sale
        # }

        with open('tmp.txt', 'a') as f:
            # f.write('{} [{}]\n'.format(name, address))
            f.write('{} [{}] USD {}:{} EUR {}:{} RUB {}:{} | {}\n'.
                    format(name, address, usd_buy, usd_sale, eur_buy, eur_sale, rub_buy, rub_sale, phones[-1]))



def get_target_html(url, useragent=None, proxy=None):
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    driver.close()
    return html