import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import json
import csv

# action 1
url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
req = requests.get(url,headers=headers)
src= req.text
# # print(src)
#
# with open('index.html','w',encoding="utf-8") as file:
#     file.write(src)


# action 2
# открываем файл и читаем
# with open('index.html', encoding="utf-8") as file:
#     src = file.read()
# создаем словарь
# all_categories_dict = {}
soup = BeautifulSoup(src, 'lxml')
# забераем все ссылки категории
all_product_href = soup.find_all(class_='mzr-tc-group-item-href')
for href in all_product_href:
    text = href.text  # текст категории
    url = 'https://health-diet.ru' + href.get('href')  # ссылка категории
    print(href)

#     # записываем сразу в словарь недавно созданный
#     all_categories_dict[text] = url
# #записываем все категории в json файл
# with open('all_cat_dict.json','w',encoding="utf-8") as file:
#     json.dump(all_categories_dict,file,indent=4,ensure_ascii=False) #indent для отступа, ensure_ascii для кодировки


# action 3
with open('all_cat_dict.json', encoding="utf-8") as file:
    all_categories = json.load(file)

iteration = int(len(all_categories)) - 1
count = 0
print(f'Всего итераций: {iteration}')
for category_name, category_href in all_categories.items():
    # символы, которые хотим заменить если они встретятся

    rep = [",", " ", "-", "'"]
    for item in rep:
        # пробегаемся по символам и ставим условие если они
        # встрятся в имени категории, заменить их на слэш
        if item in category_name:
            category_name = category_name.replace(item, '_')

    # берем все заголовки категориев
    req = requests.get(url=category_href, headers=headers)
    src = req.text
    # сохраняем каждую категорию под его же названием
    with open(f'data/{count}_{category_name}.html', 'w', encoding="utf-8") as file:
        file.write(src)
    # открываем html с категориями и читаем
    with open(f'data/{count}_{category_name}.html', encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    # проверка страницы на наличие таблицы с продуктами
    alert_blcok = soup.find(class_='uk-alert-danger')
    # если объект класса есть , переходить дальше
    if alert_blcok is not None:
        continue

    # собираем заголовки таблиц
    table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    # приравниваем их в переменную
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    urglevodi = table_head[4].text

    with open(f'data/{count}_{category_name}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow((
            product, calories, proteins, fats, urglevodi
        ))
    # собираем данные продуктов
    products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

    product_infa = []
    for i in products_data:
        # пробегаемся продуктам и по тегу td и приравниваем их в переменную
        products_tds = i.find_all('td')
        title = products_tds[0].find('a').text
        calories = products_tds[1].text
        proteins = products_tds[2].text
        fats = products_tds[3].text
        urglevodi = products_tds[4].text

        product_infa.append({
            'Title': title,
            'Calories': calories,
            'Proteins': proteins,
            'Fats': fats,
            'Urglevodi': urglevodi
        })

        # записываем  в cvs файл
        with open(f'data/{count}_{category_name}.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow((
                title,
                calories,
                proteins,
                fats,
                urglevodi
            ))
    # записываем все в json файл
    with open(f'data/{count}_{category_name}.csv', 'a', encoding='utf-8') as file:
        json.dump(product_infa, file, indent=4, ensure_ascii=False)
    count += 1
    print(f'Итерация {count}. {category_name} записан...')
    iteration -= 1
    if iteration == 0:
        print(f'Работа закончена')
        break
    print(f'Осталось итераций: {iteration}')
    sleep(random.randrange(2, 4))
