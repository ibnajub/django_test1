from django.db import models


# Create your models here.

# 1Разрабатываем каталог книг, у каждой книги обязательно есть автор, и он может быть только один.
class Catalog_author(models.Model):
    name = models.CharField(max_length=100, blank=False)


class Catalog_book(models.Model):
    name = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(Catalog_author, on_delete=models.CASCADE, related_name='cat_book')


# 2 Разработать книжную библиотеку. Храним книги, храним авторов, книгу могут написать несколько соавторов. храним кто
# брал книги, и доступна ли книга сейчас.
class Library_author(models.Model):
    name = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.name


class Library_book(models.Model):
    name = models.CharField(max_length=100, blank=False)
    author = models.ManyToManyField(Library_author)
    def __str__(self):
        return self.name


class Library_User_reader(models.Model):
    name = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.name


class Library_user_reader_history(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(Library_User_reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Library_book, on_delete=models.CASCADE)
    reading = models.BooleanField()
    def __str__(self):
        return self.user.name


class Library_allowed_book(models.Model):
    book = models.ForeignKey(Library_book, on_delete=models.CASCADE)
    allowed = models.BooleanField()
    def __str__(self):
        return self.book.name


# # 3 Разработать набор моделей, для сайта-блога, на котором можно выставлять свои статьи, комментировать чужие, ставить
# # лайк и дизлайк статье, и комментарию.
# # 3.1 Доделать так, что бы связи позволяли комментировать комментарии.
# # 3.2* Сделать лайки через GenericForeignKey
#
class Artc_user(models.Model):
    name = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.name


class Artc_article(models.Model):
    date = models.DateField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=100)
    author = models.ForeignKey(Artc_user, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.header


class Artc_likes(models.Model):
    article = models.ForeignKey(Artc_article, on_delete=models.CASCADE)
    user = models.ForeignKey(Artc_user, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    like_dislike = models.BooleanField()

    def __str__(self):
        return self.article.header


class Artc_comment(models.Model):
    parrent = models.ForeignKey('myapp.Artc_comment', null=True, blank=False, on_delete=models.DO_NOTHING)
    article = models.ForeignKey( Artc_article , on_delete=models.CASCADE)
    user = models.ForeignKey( Artc_user , on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    comment_text = models.CharField(max_length=1000)
    def __str__(self):
        return self.user.name
