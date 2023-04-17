import stanza # импортируем библиотеку NLP
import requests # для получения данных по ссылке
from bs4 import BeautifulSoup # для парсинга статьи
import re # для использования регулярных выражений

url = 'https://ria.ru/20230413/ai-1865090919.html'
page = requests.get(url).text # получаем текст статьи
soup = BeautifulSoup(page) #
text = soup.get_text()
start = text.find(url)
finish = text.find('Версия 2023.1 Beta© 2023 МИА «Россия сегодня»')
new_text = text[start:finish]
print(new_text)
# print(text)