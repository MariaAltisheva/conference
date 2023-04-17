import json

with open('lem_text_from_people.csv', 'r', encoding='UTF-8') as file:
    a = file.readlines()
    list_lem_words = a[0].split(', ')

# print(list_lem_words)
print(len(list_lem_words))

stop_words = ["Sputnik", "тема", "@content/html/head/meta[@name='og", "title']/", "description']", "быть", "заполнить", "чтобы", "Радио",
              "скриншотОтправить", "поиск", "быть"]
list_unique_words = []
for word in list_lem_words:
    if word not in list_unique_words:
        if len(word) > 3 and word not in stop_words:
            list_unique_words.append(word)

# print(list_unique_words)
print(len(list_unique_words))
dict_of_unique_words = {}
for word in list_unique_words:
    dict_of_unique_words[word] = list_lem_words.count(word)

# print(dict_of_unique_words)
dict_of_words_50 = {}
for key, values in dict_of_unique_words.items():
    if values > 50:
        dict_of_words_50[key] = values

print(len(dict_of_words_50))
# print(dict_of_words_100)

sorted_dict_of_list_words = dict(sorted(dict_of_words_50.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict_of_list_words)

with open('bag_of_words_people.csv', 'w', encoding='UTF-8') as file:
    for key, value in sorted_dict_of_list_words.items():
        for i in range(value + 1):
            file.write(key + ',')
