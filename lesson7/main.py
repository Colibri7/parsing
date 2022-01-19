import csv
import json
import os
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def get_all_pages():
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
    }
    # r = requests.get(url="https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/", headers=headers)
    #
    # if not os.path.exists('data'):
    #     os.mkdir('lesson7/data')
    #
    # with open('data/page_1.html','w',encoding='utf-8') as file:
    #     file.write(r.text)

    with open('data/page_1.html', encoding="utf8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    pages_count = int(soup.find("div", class_="bx-pagination-container").find_all("a")[-2].text)

    for i in range(1, pages_count + 1):
        url = f"https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/?PAGEN_1={i}"
        print(url)
        r = requests.get(url=url, headers=headers)
        with open(f'data/page_{i}.html', 'w', encoding='utf-8') as file:
            file.write(r.text)
        time.sleep(1)

    return pages_count + 1


def collect_data(pages_count):
    cur_date = datetime.now().strftime("%d_%m_%Y")

    with open(f'data_{cur_date}.csv', 'w') as file:
        writer = csv.writer(file)

        writer.writerow((
            'Артикул',
            'Ссылка',
            'Цена',
        ))

    data = []
    for page in range(1, pages_count):
        with open(f'data/page_{page}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        item_cards = soup.find_all("a", class_='product-item__link')

        for item in item_cards:
            product_article = item.find('p', class_='product-item__articul').text.strip()
            product_price = item.find('p', class_='product-item__price').text.lstrip('руб. ')
            product_url = f'https://shop.casio.ru/{item.get("href")}'
            # print(f'Article: {product_article} - Price: {product_price} - URL: {product_url}')

            data.append({
                'product_article': product_article,
                'product_price': product_price,
                'product_url': product_url,
            })
            with open(f'data_{cur_date}.csv', 'a') as file:
                writer = csv.writer(file)

                writer.writerow((
                   product_article,
                    product_url,
                    product_price
                ))

        print(f'[INFO] Обработана страница {page}/5')
    with open(f'data_{cur_date}.json', 'a') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    pages_count = get_all_pages()
    collect_data(pages_count=pages_count)


if __name__ == '__main__':
    main()
