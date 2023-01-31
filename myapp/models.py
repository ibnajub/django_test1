from django.db import models


# Create your models here.

# 1Разрабатываем каталог книг, у каждой книги обязательно есть автор, и он может быть только один.
class Catalog_author(models.Model):
    name = models.CharField(max_length=100, blank=False)


class Catalog_book(models.Model):
    name = models.CharField(max_length=100, blank=False)
    author = models.OneToOneField(Catalog_author, on_delete=models.CASCADE, related_name='cat_book')
#
#
# # 2 Разработать книжную библиотеку. Храним книги, храним авторов, книгу могут написать несколько соавторов. храним кто
# # брал книги, и доступна ли книга сейчас.
# class Library_author(models.Model):
#     name = models.CharField(max_length=100, blank=False)
#
#
# class Library_book(models.Model):
#     name = models.CharField(max_length=100, blank=False)
#
# class Library_book_Library_author(models.Model):
#     book = models.ForeignKey(Library_author, on_delete=models.CASCADE, related_name='l_book')
#     author = models.ForeignKey(Library_author, on_delete=models.CASCADE, related_name='l_book')
#
# class Library_User_reader(models.Model):
#     name = models.CharField(max_length=100, blank=False)
#
#
# class Library_user_reader_history(models.Model):
#     date = models.DateField(auto_now=True)
#     user = models.ForeignKey(Library_User_reader, on_delete=models.CASCADE, related_name='l_user')
#     book = models.ForeignKey(Library_book, on_delete=models.CASCADE, related_name='l_book')
#     reading = models.BooleanField()
#
#
# class Library_allowed_book(models.Model):
#     book = models.ForeignKey(Library_book, on_delete=models.CASCADE, related_name='l_book')
#     allowed = models.BooleanField()
#
#
# # 3 Разработать набор моделей, для сайта-блога, на котором можно выставлять свои статьи, комментировать чужие, ставить
# # лайк и дизлайк статье, и комментарию.
# # 3.1 Доделать так, что бы связи позволяли комментировать комментарии.
# # 3.2* Сделать лайки через GenericForeignKey
#
# class Artc_user(models.Model):
#     name = models.CharField(max_length=100, blank=False)
#
#
# class Artc_article(models.Model):
#     date = models.DateField(auto_now=True)
#     date_update = models.DateTimeField(auto_now_add=True)
#     User = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     text = models.TextField(null=True, blank=True)
#
#
# class Artc_likes(models.Model):
#     article = models.CharField(max_length=100)
#     user = models.TextField(null=True, blank=True)
#     date = models.DateTimeField(auto_now_add=True)
#     like_dislike = models.BooleanField()
#
#
# class Artc_comment(models.Model):
#     parrent = models.CharField(max_length=100)
#     article = models.CharField(max_length=100)
#     user = models.TextField(null=True, blank=True)
#     date = models.DateField(auto_now=True)
#     date_update = models.DateTimeField(auto_now_add=True)
#     comment_text = models.TextField(null=True, blank=True)
