import stanza # импортируем библиотеку NLP
import requests # для получения данных по ссылке
from bs4 import BeautifulSoup # для парсинга статьи
import re # для использования регулярных выражений


# url = 'https://habr.com/ru/companies/kaspersky/articles/725730/'
def get_text_from_url(url) -> str:
    """Получение текста по ссылке до комментарией"""
    page = requests.get(url).text # получаем текст статьи
    soup = BeautifulSoup(page) #
    text = soup.get_text()
    finish = text.find('Комментарии')
    new_text = text[:finish]
    return new_text

stop_words = ['Меню', 'Хабр', 'β', 'Поиск', 'Профиль', 'Обновить', 'Поиск', 'Профиль', 'Обновить', 'Комментарии', 'Пользователь',
              'Habr', '2006–2023,', '©', 'Facebook', 'Twitter', 'VK', 'Telegram', 'Youtube', 'Яндекс', 'Дзен', 'Язык', 'Настройка']

# def get_lem_text(new_text: str) -> list:
#     """Создание списка лемматизированных слов из строкового представления текста"""
#     ppln = stanza.Pipeline('ru', processors='tokenize,pos,lemma')
#     doc = ppln(new_text)
#     lem_text = []
#     print(*[f'word: {word.text}\tupos: {word.lemma}' for snt in doc.sentences for word in snt.words], sep='\n')
#     for snt in doc.sentences:
#         for word in snt.words:
#             lem_text.append(word.lemma)
#     return lem_text

    # print(lem_text)
def write_file(lem_text: list) -> None:
    "Запись данных в файл csv"
    with open('lem_text.csv', 'a', encoding='UTF-8') as file:
        for i in lem_text:
            if len(i) > 1 and re.search('[0-9]', i) is None and i not in stop_words:
                file.write(i + ', ')


list_of_url = []
with open('urls.csv', 'r') as file:
    for line in file.readlines():
        list_of_url.append(line.strip())
text_list = [] # список текстов
for url in list_of_url:
    text_list.append(get_text_from_url(url))

big_text = ' '.join(text_list)

# list_of_lem_words = []

ppln = stanza.Pipeline('ru', processors='tokenize,pos,lemma')
doc = ppln(big_text)
lem_text = [] # список лемматизированных слов
# print(*[f'word: {word.text}\tupos: {word.lemma}' for snt in doc.sentences for word in snt.words], sep='\n')
for snt in doc.sentences:
    for word in snt.words:
        lem_text.append(word.lemma)

with open('lem_text.csv', 'w', encoding='UTF-8') as file:
    for i in lem_text:
        if len(i) > 1 and re.search('[0-9]', i) is None and i not in stop_words:
            file.write(i + ', ')


