from stanza_2 import get_text_from_url, get_lem_text, write_file



list_of_url = []
with open('urls.csv', 'r') as file:
    for line in file.readlines():
        list_of_url.append(line.strip())

print(list_of_url)

text_list = []
for url in list_of_url:
    text_list.append(get_text_from_url(url))

list_of_lem_words = []
for text in text_list:
    list_of_lem_words.append(get_lem_text(text))

for list_ in list_of_lem_words:
    write_file(list_)




