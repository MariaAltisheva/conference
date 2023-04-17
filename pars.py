import requests
from bs4 import BeautifulSoup
import re


url = 'https://habr.com/ru/companies/kaspersky/articles/725730/'
page = requests.get(url).text
soup = BeautifulSoup(page)
text = soup.get_text()
# print(headline)
# p_tags = soup.find_all('p')
# print(p_tags)
# p_tags_text = [tag.get_text().strip() for tag in p_tags]
# sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
# sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
# print(sentence_list)
# article = ' '.join(sentence_list)
# print(article)
# print(type(text))
# print(text)
finish = text.find('Комментарии')
new_text = text[:finish]
print(type(new_text))
print(new_text)
# print(new_text)
new_text = text.split(' ')
# print(new_text)
new_text2 = []
stop_words = ['Меню', 'Хабр', 'β', 'Поиск', 'Профиль', 'Обновить', 'Поиск', 'Профиль', 'Обновить', 'Комментарии', 'Пользователь',
              'Habr', '2006–2023,', '©', 'Facebook', 'Twitter', 'VK', 'Telegram', 'Youtube', 'Яндекс', 'Дзен', 'Язык', 'Настройка']
for i in new_text:
    if '\n' not in i and i != '':
        new_text2.append(i.strip())
# print(new_text2)
new_text3 = []
for word in new_text2:
    if word not in stop_words:
        if len(word) > 1:
            if re.search('[a-zA-Z0-9]', word) is None:
                new_text3.append(word)

print(new_text3)
new_text4 = []
for word in new_text3:
    a = word.find(',')
    b = word.find('.')
    c = word.find(',')
    d = word.find('-')
    if a == -1 and b == -1 and c == -1 and d == -1:
        new_text4.append(word)
    # else:
    #     new_text4.append(word[:a])

print(' '.join(new_text4))

# new_text3 = ' '.join(new_text2)
# print(new_text3)

# if __name__ == '__main__':
#     pass