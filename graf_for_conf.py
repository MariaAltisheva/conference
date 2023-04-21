import matplotlib.pyplot as plt
from stopwords import get_stopwords

STOPWORDS = get_stopwords('russian')

graf_habr_dict = {'быть': 1650, 'ChatGPT': 1567, 'мочь': 1223, 'который': 1099, 'этот': 920, 'модель': 712, 'ответ': 617, 'использовать': 548, 'если': 468, 'можно': 461, 'такой': 458, 'данные': 450, 'текст': 439, 'задача': 435, 'вопрос': 417, 'свой': 409, 'писать': 393, 'делать': 389, 'чтобы': 389, 'весь': 379, 'человек': 379, 'работа': 353, 'запрос': 347, 'время': 334, 'один': 333, 'другой': 306, 'только': 285, 'также': 282, 'нужный': 280, 'пользователь': 272, 'более': 270, 'пример': 269, 'результат': 257, 'обучение': 255, 'получить': 253, 'количество': 252, 'информация': 251, 'интеллект': 242, 'самый': 242, 'решение': 242, 'нейросеть': 240, 'статья': 237, 'новый': 237, 'система': 232, 'использование': 222, 'слово': 221, 'язык': 219, 'проблема': 215, 'простой': 212, 'каждый': 209, 'хороший': 208, 'даже': 207, 'первый': 206, 'себя': 206, 'например': 202, 'работать': 200, 'какой': 198, 'компания': 196, 'просить': 191, 'просто': 184, 'несколько': 184, 'очень': 183, 'добавить': 182, 'хотеть': 176, 'должен': 174, 'помощь': 173, 'возможность': 172, 'когда': 171, 'большой': 169, 'много': 168, 'OpenAI': 165, 'следующий': 165, 'иметь': 160, 'языковой': 159, 'процесс': 159, 'поэтому': 156, 'return': 151, 'ошибка': 150, 'приложение': 150, 'являться': 149, 'сервис': 149, 'создать': 148, 'давать': 148, 'случай': 147, 'качество': 147, 'решить': 146, 'уровень': 146, 'некоторый': 144, 'искусственный': 143, 'создание': 141, 'здесь': 141, 'генерировать': 141, 'стать': 140, 'проект': 138, 'Wolfram': 138, 'контекст': 137, 'сложный': 136, 'найти': 136, 'знать': 135, 'всего': 135, 'технология': 133, 'помочь': 133, 'минута': 131, 'часть': 131, 'бота': 131, 'создавать': 128, 'тема': 128, 'дело': 126, 'данный': 126, 'основа': 124, 'строка': 124, 'после': 122, 'import': 122, 'пока': 122, 'поиск': 121, 'необходимый': 120, 'однако': 119, 'инструмент': 119, 'функция': 119, 'пробовать': 117, 'база': 116, 'разработчик': 116, 'любой': 115, 'сеть': 114, 'профиль': 112, 'версия': 112, 'просмотр': 111, 'область': 111, 'обновить': 110, 'генерация': 110, 'Гугл': 109, 'интересный': 108, 'позволять': 107, 'далее': 107, 'важный': 106, 'разный': 106, 'голос': 106, 'меню': 105, 'прочтение': 105, 'говорить': 105, 'число': 105, 'понимать': 105, 'видеть': 104, 'момент': 104, 'разработка': 104, 'технический': 103, 'больше': 102, 'вариант': 102, 'диалог': 102, 'сайт': 100, 'сейчас': 100, 'закладка': 100, 'сказать': 100, 'файл': 99, 'Хаба': 99, 'тест': 99, 'различный': 98, 'получать': 97, 'именно': 97, 'теперь': 95, 'вывод': 94, 'доступ': 94, 'хотя': 94, 'машинный': 94, 'элемент': 94, 'общий': 93, 'документ': 92, 'игра': 92, 'смотреть': 90, 'знание': 89, 'через': 89, 'мышление': 89, 'способный': 88, 'параметр': 88, 'решать': 88, 'задать': 88, 'метод': 88, 'способ': 88, 'английский': 87, 'анализ': 87, 'ссылка': 87, 'эксперт': 87, 'комментарий': 87, 'подход': 86, 'точка': 86, 'private': 85, 'цель': 85, 'правильный': 84, 'that': 84, 'источник': 84, 'образ': 84, 'сгенерировать': 84, 'стоить': 84, 'значение': 84, 'доска': 84, 'критический': 84, 'заключение': 83, 'алгоритм': 82, 'уметь': 82, 'from': 82, 'оценка': 82, 'тега': 82, 'привести': 82, 'начать': 81, 'программа': 81, 'всегда': 81, 'часто': 81, 'дать': 81, 'автор': 81, 'сложность': 80, 'понять': 80, 'with': 79, 'конкретный': 78, 'написание': 78, 'сообщение': 78, 'описание': 78, 'список': 78, 'display': 78, 'получиться': 77, 'подобный': 77, 'проверить': 77, 'полезный': 77, 'возможный': 77, 'идея': 76, 'реальный': 76, 'выдавать': 76, 'чат-бота': 76, 'способность': 75, 'Language': 75, 'основной': 75, 'похожий': 74, 'сторона': 74, 'будущее': 74, 'вообще': 74, 'board': 74, 'затем': 73, 'развитие': 73, 'player': 73, 'конечно': 72, 'потому': 72, 'существовать': 71, 'предлагать': 71, 'chatGPT': 71, 'целое': 70, 'библиотека': 70, 'надо': 70, 'содержать': 70, 'что-то': 70, 'брать': 70, 'отвечать': 70, 'продукт': 70, 'тоже': 69, 'навык': 69, 'программирование': 68, 'думать': 68, 'this': 68, 'русский': 68, 'выполнять': 68, 'пытаться': 68, 'готовый': 68, 'ограничение': 68, 'data': 68, 'быстро': 67, 'Python': 67, 'второй': 67, 'какой-то': 67, 'условие': 67, 'задание': 67, 'студент': 66, 'почему': 66, 'название': 66, 'равный': 66, 'н-лат': 66, 'идти': 65, 'сразу': 65, 'между': 65, 'день': 65, 'помогать': 64, 'доступный': 64, 'предложение': 64, 'объем': 64, 'указать': 64, 'ответить': 64, 'объект': 64, 'заменить': 64, 'опыт': 64, 'показать': 63, 'хорошо': 63, 'представить': 63, 'программист': 63, 'связать': 63, 'клиент': 63, 'type': 63, 'выглядеть': 62, 'инструкция': 62, 'письмо': 62, 'команда': 62, 'оказаться': 62, 'исследование': 62, 'считать': 62, 'действительно': 61, 'проверка': 61, 'начало': 61, 'начинать': 61, 'move': 60, 'далеко': 59, 'применение': 59, 'обучить': 59, 'смысл': 59, 'книга': 59, 'архитектура': 59, 'предыдущий': 58, 'последний': 58, 'правило': 58, 'описать': 58, 'требоваться': 58, 'пройти': 58, 'чат-бот': 58, 'жизнь': 57, 'история': 57, 'внимание': 57, 'достаточно': 57, 'точно': 57, 'иногда': 57, 'учитель': 57, 'your': 57, 'специалист': 56, 'известный': 56, 'ничто': 56, 'нейронный': 56, 'предложить': 56, 'высокий': 56, 'исходный': 56, 'текущий': 56, 'поисковый': 55, 'сервер': 55, 'требование': 55, 'интернет': 55, 'итог': 55, 'получение': 55, 'собственный': 55, 'средний': 55, 'интерфейс': 55, 'человеческий': 55, 'понятный': 54, 'возможно': 54, 'мнение': 54, 'позиция': 54, 'естественный': 54, 'чата': 54, 'public': 54, 'else': 54, 'лишь': 53, 'поддержка': 53, 'have': 53, 'настоящий': 53, 'рабочий': 53, 'задавать': 53, 'конец': 53, 'искать': 53, 'class': 53, 'print(': 53, 'self': 53, 'пользоваться': 52, 'следовать': 52, 'перевод': 52, 'дополнительный': 52, 'место': 52, 'из-за': 52, 'набор': 52, 'месяц': 52, 'справиться': 52, 'научный': 52, 'ведь': 52, 'план': 52, '*искусственный': 51, 'скорее': 51, 'prompt': 51, 'will': 51, 'немного': 51, 'прийтись': 51, 'определить': 51, 'экспертиза': 51}
graf_ria_dict = {'тема': 1256, 'Россия': 591, 'искусственный': 402, 'интеллект': 389, 'ChatGPT': 379, 'сегодня': 325, 'Новость': 311, 'новый': 228, 'сообщение': 225, 'компания': 221, 'вопрос': 218, 'технология': 205, 'форма': 200, 'человек': 194, 'нейросеть': 189, 'связь': 173, 'пароль': 162, 'данные': 160, 'главный': 158, 'радио': 154, 'отправить': 153, 'чат-бот': 139, 'мочь': 136, 'поле': 132, 'писать': 129, 'если': 127, 'заполнить': 126, 'российский': 122, 'материал': 122, 'хотеть': 118, 'развитие': 113, 'почта': 110, 'стать': 109, 'система': 109, 'обязательный': 108, 'заполнение': 108, 'Гугл': 104, 'говорить': 100, 'назад': 99, 'страна': 98, 'делать': 95, 'чтобы': 94, 'обратный': 94, 'экономика': 94, 'модель': 91, 'использование': 90, 'связаться': 90, 'ответ': 89, 'пользователь': 89, 'американский': 88, 'использовать': 86, 'ошибка': 85, 'должен': 84, 'программа': 83, 'заявить': 83, 'создать': 82, 'проблема': 82, 'аккаунт': 81, 'работа': 80, 'возможность': 80, 'OpenAI': 78, 'восстановление': 78, 'сообщать': 77, 'эксперт': 77, 'банк': 77, 'такой': 77, 'эфир': 75, 'ученый': 74, 'глава': 74, 'войти': 74, 'новость': 73, 'считать': 73, 'ссылка': 72, 'который': 72, 'блокировка': 72, 'удалить': 72, 'текст': 71, 'Радио': 71, 'сообщить': 71, 'слово': 70, 'решение': 70, 'область': 69, 'конец': 69, 'русский': 69, 'основа': 68, 'готовый': 68, 'информация': 68, 'цифровой': 68, 'информационный': 66, 'мировой': 66, 'принимать': 66, 'рубль': 66, 'доллар': 66, 'Украина': 65, 'пользоваться': 65, 'международный': 64, 'сайт': 64, 'чат-бота': 63, 'агентство': 63, 'нужный': 63, 'другой': 62, 'задача': 62, 'федеральный': 62, 'блокировать': 62, 'один': 61, 'угроза': 61, 'способ': 61, 'президент': 60, 'Микрософт': 60, 'отвечать': 59, 'получить': 59, 'рынок': 59, 'дело': 59, 'Маск': 58, 'государственный': 58, 'конфиденциальность': 58, 'адрес': 58, 'выбрать': 58, 'апрель': 57, 'согласный': 57, 'часть': 56, 'Яндекс': 56, 'Клименко': 55, 'автор': 54, 'сфера': 54, 'помочь': 54, 'доступ': 54, 'россиянин': 54, 'город': 54, 'разблокировать': 54, 'низко': 54, 'перетать': 54, 'скриншотОтправить': 54, 'поиск': 54, 'работать': 54, 'быть': 54, 'актив': 54, "@content/html/head/meta[@name='og": 53, "description']": 53, 'научный': 53, 'Илон': 52, "title']/": 52, 'март': 52, 'риск': 52, 'закон': 52, 'условие': 52, 'машина': 52, 'документ': 51, 'бизнес': 51, 'какой': 51, 'конфликт': 51}

graf_habr_x = []
graf_habr_y = []

i = 0
for key, value in graf_habr_dict.items():
    if i < 20 and key not in STOPWORDS:

        graf_habr_x.append(key)
        graf_habr_y.append(value)
        i += 1




# x_c = [1, 2, 3]
# y_c = [0, 3, 1]

plt.plot(graf_habr_x, graf_habr_y)
plt.xticks(rotation=45)
plt.show()