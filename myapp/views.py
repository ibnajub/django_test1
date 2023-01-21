from django.shortcuts import render

# mysite/myapp/views.py
from django.http import HttpResponse


# Поздравляю, это ваш первый контроллер, который может, принять запрос, и отдать ответ с текстом, больше ничего
def main(request):
    return HttpResponse("Hey! It's your main view!!")

def another(request):
    return HttpResponse("It's another page!!")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id):
    return HttpResponse(f"This is an article #{article_id}.")
def article_slug(request, article_id, slug_text):
    return HttpResponse(f"This is an article #{article_id}. slug #{slug_text}")


def user_id(request, user_number):
    return HttpResponse(f"This is an user #{user_number}.")



def regex_1(request):
    return HttpResponse(f"it's regexp ")
def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")

