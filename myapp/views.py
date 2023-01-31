from django.shortcuts import render
import random
import string

# mysite/myapp/views.py
from django.http import HttpResponse


# Поздравляю, это ваш первый контроллер, который может, принять запрос, и отдать ответ с текстом, больше ничего
def main(request):
    return HttpResponse("Hey! It's your main view!!")


def another(request):
    return HttpResponse("It's another page!!")


def main_article(request):
    return render(request, 'articles.html', {

    })


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id):
    # return HttpResponse(f"This is an article #{article_id}.")
    return render(request, 'article.html', {
        'article_id': article_id,
    })


def article_slug(request, article_id, slug_text):
    # return HttpResponse(f"This is an article #{article_id}. slug #{slug_text}")
    return render(request, 'article.html', {
        'article_id': article_id,
        'slug_text': slug_text,
    })


def user_id(request, user_number):
    return HttpResponse(f"This is an user #{user_number}.")


def regex_1(request):
    return HttpResponse(f"it's regexp")


def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")


# -----------------------------------


# class MyClass:
#     string = ''
#
#     def __init__(self, s):
#         self.string = s


def index(request):
    # my_num = 33
    # my_str = 'some string'
    # my_dict = {"some_key": "some_value"}
    # my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    # my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    # my_class = MyClass('class string')
    # rand_list_article = [1, 2, 3, 4, 5]
    rand_id = 'id'
    rand_slag = 'slag'
    # # rand_list_article = 2
    # letters = string.ascii_letters
    # rand_article_slag = ''.join(random.choice(letters) for i in range(5)) + '-' \
    #                     + ''.join(random.choice(letters) for i in range(5))
    return render(request, 'index.html', {
        # 'rand_list_article': rand_list_article,
        # 'rand_article_slag': rand_article_slag,
        'rand_id': rand_id,
        'rand_slag': rand_slag,

    })
