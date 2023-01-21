"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
from django.urls import path, include, re_path
from myapp.views import main, main_article, uniq_article, article, article_slug,  regex_1

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', main),
    path('article/', main_article),
    path('article/archive/', uniq_article),

    path('users/', include('myapp.urls')),

    # http://127.0.0.1:8000/article/<int:article_number>,
    path('article/<int:article_id>/', article, name='article'),

    # http://127.0.0.1:8000/article/<int:article_number>/archive,
    path('article/<int:article_id>/archive/', article, name='article'),

    # http://127.0.0.1:8000/article/<int:article_number>/<slug:slug_text>,
    path('article/<int:article_id>/<slug:slug_text>/', article_slug, name='article'),

    # https://www.exlab.net/tools/sheets/regexp.html

    # Создать урл который будет принимать параметр вида 4 символа от 1 до 9, или от a до f, знак дефиса и еще 6 символов
    # , например /34f1-1ac498/
    re_path('^[0-9a-f]{4}\-[0-9a-f]{6}$', regex_1),


    # Создать урл который будет принимать в качестве параметра корректный номер украинского мобильного телефона,
    # 0501231211 - корректно, 0751231212 - нет
]
