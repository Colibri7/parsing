import json
import requests
from bs4 import BeautifulSoup

# news_list =  []
# for i in range(0,451,15):
#     src = f'https://www.skiddle.com/news/festivals/{i}'
#
#     q = requests.get(src)
#     result = q.content
#     soup = BeautifulSoup(result, 'lxml')
#
#     news = soup.find_all(class_='card-img-link')
#     for i in news:
#         news_page_url = "https://www.skiddle.com"+i.get('href')
#         news_list.append(news_page_url)
# print(news_list)
# with open('news_list.txt','a',encoding='utf-8') as file:
#     for line in news_list:
#         file.write(f'{line}\n')


with open('news_list.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    # пустой список для данных всех людей
    data_dict = []
    count = 0
    for line in lines:

        q = requests.get(line)  # в i передается ссылка на новость
        result = q.content
        soup = BeautifulSoup(result,'lxml')
        new = soup.find(class_='grid').find('h1',class_='h2').text
        date = soup.find(class_='grid bg-white').find('p').text
        data = {
            'title': new,
            'date': date

        }
        count += 1
        print(f'#{count}: {line} is done!')
        data_dict.append(data)
        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)