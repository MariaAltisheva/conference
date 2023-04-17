# pip install pymorphy2
import pymorphy2
from pars import new_text4

morph = pymorphy2.MorphAnalyzer()
words = ['грустно', 'зависимость', 'хорошему', 'приводит', 'альтернатив']
try:
    for word in words:
        p = morph.parse(word)[0]
        print(p.normal_form)
except:
    pass