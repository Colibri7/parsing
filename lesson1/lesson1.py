import re

from bs4 import BeautifulSoup

with open('blank/index.html', encoding='utf-8') as file:
    src = file.read()
# print(src)
soup = BeautifulSoup(src, "lxml")

# ищет тег title
# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# ищет первый попавшийся h1 тег
# page1_h1=soup.find('h1')
# print(page1_h1.text)

# ищет все теги с h1
# page1_h1_all=soup.find_all("h1")
# for i in page1_h1_all:
#     print(i.text)

# ищет тег div с классом user__name
# user_name = soup.find('div',class_='user__name')
# print(user_name.text.strip())


# user_name = soup.find('div',class_='user__name').find('span').text
# print(user_name)

# тоже самое, только в словаре
# user_name = soup.find('div',{'class':'user__name','id':'aaa'}).find('span').text
# print(user_name)

# ищет все теги span в классе user__info
# find_all_span_in_user_info = soup.find(class_='user__info').find_all("span")
# for i in find_all_span_in_user_info:
#     print(i.text)
# print(find_all_span_in_user_info[0].text)


# social_links = soup.find(class_='social__networks').find('ul').find_all('a')
# print(social_links)

# ищет все теги a
# all_a = soup.find_all('a')
# for url in all_a:
#     item_url= url.get('href') # get берет url
#     item_text= url.text # берет текст
#     print(f'{item_text} -> {item_url}')


# post_div = soup.find(class_='post__text').find_parent('div','user__post')
# print(post_div)


# next_el = soup.find(class_='post__title').next_element.next_element.text
# print(next_el)
# next_el = soup.find(class_='post__title').find_next().text
# print(next_el)

# ищет div с классом post__title и печатает послее него идуший div
# next_sibling = soup.find(class_='post__title').find_next_sibling()
# print(next_sibling)

# ищет класс some__links и берет все теги a
# links = soup.find(class_='some__links').find_all('a')
# for i in links:
#     a_href = i.get('href')
#     a_href1 = i['href']
#     a_href_data = i.get('data-attr')
#     a_href_data1 = i["data-attr"]
#     print(a_href1)
#     print(a_href_data1)

# ищет по тексту , нужно учесть, что в find надо писать целый текст
# find_by_text = soup.find('a',text='Одежда для взрослых')
# print(find_by_text.text)

# ищет все текста где есть слово Одежда
# find_by_text = soup.find('a',text=re.compile('Одежда'))
# print(find_by_text.text)

# ищет все текста где есть слово Одежда в нижнем или же вверхнем регистре
# find_all_by_word = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_all_by_word)

