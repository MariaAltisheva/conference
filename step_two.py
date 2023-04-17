import json

with open('lem_text.csv', 'r', encoding='UTF-8') as file:
    a = file.readlines()
    list_lem_words = a[0].split(', ')

# print(list_lem_words)
print(len(list_lem_words))

list_unique_words = []
for word in list_lem_words:
    if word not in list_unique_words:
        if len(word) > 3:
            list_unique_words.append(word)

# print(list_unique_words)
print(len(list_unique_words))
dict_of_unique_words = {}
for word in list_unique_words:
    dict_of_unique_words[word] = list_lem_words.count(word)

# print(dict_of_unique_words)
dict_of_words_100 = {}
for key, values in dict_of_unique_words.items():
    if values > 50:
        dict_of_words_100[key] = values

print(len(dict_of_words_100))
# print(dict_of_words_100)

sorted_dict_of_list_words = dict(sorted(dict_of_words_100.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict_of_list_words)


