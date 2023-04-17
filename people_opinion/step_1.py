import stanza # импортируем библиотеку NLP
import requests # для получения данных по ссылке
from bs4 import BeautifulSoup # для парсинга статьи
import re # для использования регулярных выражений

url = 'https://radiosputnik.ria.ru/20230414/1865371423.html'
page = requests.get(url).text # получаем текст статьи
soup = BeautifulSoup(page) #
text = soup.get_text()
start = text.find(url)
finish = text.find('Прямой эфирВ эфиреПодкасты – Радио Sputnik')
new_text = text[start:finish]
print(new_text)
    # finish = text.find('Комментарии')
    # new_text = text[:finish]
