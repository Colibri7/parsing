import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    }

    r = requests.get(url=url, headers=headers)
    with open('index.html', 'w') as file:
        file.write(r.text)

    # get hotels urls
    r = requests.get('https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most', headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    # собираем каждую ссылку отеля в блоках
    hotels_card = soup.find_all('div', class_='hotel_card_dv')
    for url in hotels_card:
        # забираем ссылку с помощью атрибута get
        hotel_url = url.find("a").get('href')
        print(hotel_url)


def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override',
                           'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36')
    try:
        driver = webdriver.Firefox(
            executable_path="\lesson6\geckodriver.log",options=options
        )
        driver.get(url=url)
        time.sleep(5)
        with open('index_selenium.html', 'w') as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    # get_data('https://tury.ru/hotel/most_luxe.php')
    get_data_with_selenium('https://tury.ru/hotel/most_luxe.php')

if __name__ == '__main__':
    main()
