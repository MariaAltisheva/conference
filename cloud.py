import pandas as pd
import matplotlib.pyplot as plt
# загружаем класс WordCloud из библиотеки wordcloud
from wordcloud import WordCloud

data = pd.read_csv("lem_text.csv")
text = ' '.join(data)

# Генерируем облако слов и сохраняем в переменной cloud
cloud = WordCloud().generate(text)
# Выводим облако слов на экран
plt.imshow(cloud)
# Отключаем отображение осей
plt.axis('off')