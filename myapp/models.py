from django.db import models
# Create your models here.

# 1Разрабатываем каталог книг, у каждой книги обязательно есть автор, и он может быть только один.
class Author1(models.Model):
    name = models.CharField(max_length=100)


class Book1(models.Model):
    name = models.CharField(max_length=100)


# 2 Разработать книжную библиотеку. Храним книги, храним авторов, книгу могут написать несколько соавторов. храним кто
# брал книги, и доступна ли книга сейчас.
class Author2(models.Model):
    name = models.CharField(max_length=100)


class Book2(models.Model):
    name = models.CharField(max_length=100)

class User_reader(models.Model):
    name = models.CharField(max_length=100)

class User_reader_history(models.Model):
    date = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    readeng = models.BooleanField()
class allowed_books(models.Model):
    book = models.CharField(max_length=100)
    allowed = models.BooleanField()


# 3 Разработать набор моделей, для сайта-блога, на котором можно выставлять свои статьи, комментировать чужие, ставить
# лайк и дизлайк статье, и комментарию.
# 3.1 Доделать так, что бы связи позволяли комментировать комментарии.
# 3.2* Сделать лайки через GenericForeignKey

class User(models.Model):
    name = models.CharField(max_length=100)
class Article(models.Model):
    date = models.CharField(max_length=100)
    User = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)


class Likes(models.Model):
    article = models.CharField(max_length=100)
    user = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=100)
    like_dislike = models.TextField(null=True, blank=True)

class Comment(models.Model):
    parrent = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    user = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=100)
    comment_text = models.TextField(null=True, blank=True)