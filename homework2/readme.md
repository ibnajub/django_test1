pip freeze > requirements.txt  
pip install -r requirements.txt
python manage.py createsuperuser

VSCode Django https://code.visualstudio.com/docs/python/tutorial-django

Вопросы для собесов:
Паттерн
ООП
ACID SOLID Нормализация БД
SOLID https://medium.com/webbdev/solid-4ffc018077da
https://habr.com/ru/companies/productivity_inside/articles/505430/
МэжикМетоды
СинглТон
ЧериПик
Каталог паттернов проектирования
https://refactoring.guru/ru/design-patterns/catalog

Урок 1
https://github.com/PonomaryovVladyslav/PythonCources/blob/master/lesson28.md
https://www.exlab.net/tools/sheets/regexp.html
https://regex101.com/
./pic/regexp.png

https://bool.dev/blog/detail/vizualizatsiya-poleznykh-git-komand
https://learngitbranching.js.org/?locale=ru_RU

Урок 2
https://github.com/PonomaryovVladyslav/PythonCources/blob/master/lesson29.md
https://docs.djangoproject.com/en/2.2/ref/templates/builtins/
Домашнее задание / Практика
Создать базовую html от которой будут наследоваться все остальные
Для статических урлов сделать html файлы наследующиеся от базового, но с разным текстом (можно и оформлением)

Для
урлов http://127.0.0.1:8000/article/<int:article_number>, http://127.0.0.1:8000/article/<int:article_number>/<slug:slug_text>,
Сделать html файлы в которых выводить текст о том чётный введен или нечётный article_number (логику прописать в
темплейтах),
если введён slug_text, выводить этот текст при помощи include в добавочной html (добавленной из отдельного файла).

На главной странице (http://127.0.0.1:8000/) сделать две ссылки, перейти на случайную статью (id), и перейти
на случайную статью со случайным слагом (5-10 случайных символов)

На всех страницах внизу должна быть ссылка на главную.

https://www.educative.io/answers/how-to-generate-a-random-string-in-python

How to manage static files (e.g. images, JavaScript, CSS)¶
https://docs.djangoproject.com/en/4.1/howto/static-files/

Урок 3 ОРМ

