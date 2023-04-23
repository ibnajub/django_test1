"""
URL configuration for homework2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
# from django.urls import path
from django.urls import path, include, re_path
from myapp.views import uniq_article, article, article_slug, regex, index, main_article, blogs, topics, topic, blog

# from ormTest.views import hotline

# alt+ enter вставка импорта
urlpatterns = [
    
    path('', index, name='index'),
    
    path('admin/', admin.site.urls),
    # path('', main),
    # path('hotline/', hotline, name='hotline'),  #
    
    path('articles/', main_article, name='articles'),
    # path('article/archive/', uniq_article),
    #
    # path('users/', include('myapp.urls')),
    # # http://127.0.0.1:8000/users/<int:user_number>
    # path('<int:user_number>/', user_id, name='users'),
    #
    # http://127.0.0.1:8000/article/<int:article_number>,
    path('article/<int:article_id>/', article, name='article_id'),
    #
    # # http://127.0.0.1:8000/article/<int:article_number>/archive,
    # path('article/<int:article_id>/archive/', article, name='article_id'),
    #
    # http://127.0.0.1:8000/article/<int:article_number>/<slug:slug_text>,
    path('article/<int:article_id>/<slug:slug_text>/', article_slug, name='article_slug'),
    
    # # https://www.exlab.net/tools/sheets/regexp.html
    #
    # # Создать урл который будет принимать параметр вида 4 символа от 1 до 9, или от a до f, знак дефиса и еще 6 символов
    # # , например /34f1-1ac498/
    # # re_path('^[0-9a-f]{4}\-[0-9a-f]{6}$', regex_1),
    # re_path(r'^(?P<text>^[0-9a-f]{4}\-[0-9a-f]{6}$$)', regex),
    #
    # # Создать урл который будет принимать в качестве параметра корректный номер украинского мобильного телефона,
    # # 0501231211 - корректно, 0751231212 - нет
    # re_path(r'^(?P<text>^\A(0(39|67|68|96|97|98|50|66|95|99|63|73|93)\d{7})\Z$)', regex),
    
    # домашня сторінка сайту. Він міститиме список блогів, доступних на сайті django
    path('blogs/', blogs, name='blogs'),
    path('topics/', topics, name='topics'),
    path('topic/<int:topic_id>', topic, name='topic'),
    
    # надає звичайний текст для користувача, що описує функції сайту django.
    path('about/', index, name='about'),
    
    # детальний перегляд окремої публікації в блозі. URL-адреса містить динамічну частину. Це буде використано для
    # отримання однієї публікації блогу з бази даних.
    path('<slug:slug>/', blog, name='blog_slug'),
    
    # це подання використовуватиметься для додавання коментарів до публікації блогу.
    path('<slug:slug>/comment/', index, name='comment'),
    
    # це подання використовуватиметься для додавання коментарів до публікації блогу.
    path('create/', index, name='create'),
    
    # перегляд для оновлення наявних даних публікації.
    path('<slug:slug>/update/', index, name='update'),
    
    # перегляд для підтвердження видалення публікації.
    path('<slug:slug>/delete/', index, name='delete'),
    
    # Персональна сторінка користувача.
    path('profile/<str:username>/', index, name='profile_username'),
    
    # Ця сторінка використовуватиметься для зміни облікових даних користувачів.
    path('change_password/', index, name='change_password'),
    
    # Сторінка з формою для реєстрації нового користувача.
    path('register/', index, name='register'),
    
    # Сторінка з формою для логіна.
    path('login/', index, name='login'),
    
    # Логаут. Має перенаправляти користувача назад на домашню сторінку..
    path('logout/', index, name='logout'),

]
