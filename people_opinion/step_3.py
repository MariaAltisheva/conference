import requests # для получения данных по ссылке
from bs4 import BeautifulSoup # для парсинга статьи
import re # для использования регулярных выражений
import stanza # импортируем библиотеку NLP
from stopwords import get_stopwords

STOPWORDS_RU = get_stopwords('russian')

def get_text_from_urls(list_of_urls):
    list_of_text_people = []
    for url_ in list_of_urls:
        try:
            if 'radiosputnik.ria.ru' in url_:
                page = requests.get(url_).text  # получаем текст статьи
                soup = BeautifulSoup(page)  #
                text = soup.get_text()
                start = text.find(url_)
                finish = text.find('Прямой эфирВ эфиреПодкасты – Радио Sputnik')
                new_text = text[start:finish]
                list_of_text_people.append(new_text)
            else:
                page = requests.get(url_).text  # получаем текст статьи
                soup = BeautifulSoup(page)  #
                text = soup.get_text()
                start = text.find(url_)
                finish = text.find('Версия 2023.1 Beta© 2023 МИА «Россия сегодня»')
                new_text = text[start:finish]
                list_of_text_people.append(new_text)
        except:
            pass
    list_of_text_people = ' '.join(list_of_text_people)
    list_of_text_people = list_of_text_people.split()
    return list_of_text_people

list_of_urls_people = []
with open('urls_people.csv', 'r') as file:
    for line in file.readlines():
        list_of_urls_people.append(line.strip())

# print(list_of_urls_people)

# print(get_text_from_urls(list_of_urls_people))
list_words_all = get_text_from_urls(list_of_urls_people)
just_normal_words = []
for words in list_words_all:
    if words not in STOPWORDS_RU and len(words) > 3:
        just_normal_words.append(words)

big_text = ' '.join(just_normal_words)

ppln = stanza.Pipeline('ru', processors='tokenize,pos,lemma')
doc = ppln(big_text)
lem_text = [] # список лемматизированных слов
# print(*[f'word: {word.text}\tupos: {word.lemma}' for snt in doc.sentences for word in snt.words], sep='\n')
for snt in doc.sentences:
    for word in snt.words:
        lem_text.append(word.lemma)

with open('lem_text_from_people.csv', 'w', encoding='UTF-8') as file:
    for i in lem_text:
        if len(i) > 1 and re.search('[0-9]', i) is None:
            file.write(i + ', ')

