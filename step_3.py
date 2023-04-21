from stopwords import get_stopwords

STOPWORDS_RU = get_stopwords('russian')

with open('lem_text.csv', 'r', encoding='UTF-8') as file:
    a = file.readlines()
    list_lem_words = a[0].split(', ')

print(len(list_lem_words))

list_unique_words = list(set(list_lem_words))
print(len(list_unique_words))
# print(list_unique_words)
#
# usual_words = ['быть', 'этот', 'если', 'такой', 'чтобы', 'весь', 'также']
dict_of_unique_words = {}
for word in list_unique_words:
    if len(word) > 3 and word not in STOPWORDS_RU:
        dict_of_unique_words[word] = list_lem_words.count(word)
#
# print(dict_of_unique_words)
dict_of_words_50 = {}
for key, values in dict_of_unique_words.items():
    if values > 50:
        dict_of_words_50[key] = values
#
print(len(dict_of_words_50))
# print(dict_of_words_30)

sorted_dict_of_list_words = dict(sorted(dict_of_words_50.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict_of_list_words)

with open('bag_of_words.csv', 'w', encoding='UTF-8') as file:
    for key, value in sorted_dict_of_list_words.items():
        for i in range(value + 1):
            file.write(key + ',')
