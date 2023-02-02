from django.db import models


# Create your models here.
# 1Разрабатываем каталог книг, у каждой книги обязательно есть автор, и он может быть только один.
class CatalogAuthor(models.Model):
    name = models.CharField(max_length=100, blank=False)


class CatalogBook(models.Model):
    name = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(CatalogAuthor, on_delete=models.CASCADE, related_name='cat_book')


# 2 Разработать книжную библиотеку. Храним книги, храним авторов, книгу могут написать несколько соавторов. храним кто
# брал книги, и доступна ли книга сейчас.
class LibraryAuthor(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class LibraryBook(models.Model):
    name = models.CharField(max_length=100, blank=False)
    author = models.ManyToManyField(LibraryAuthor)

    def __str__(self):
        return self.name


class LibraryUserReader(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class LibraryUserReaderHistory(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(LibraryUserReader, on_delete=models.CASCADE)
    book = models.ForeignKey(LibraryBook, on_delete=models.CASCADE)
    reading = models.BooleanField()

    def __str__(self):
        return self.user.name


class LibraryAllowedBook(models.Model):
    book = models.ForeignKey(LibraryBook, on_delete=models.CASCADE)
    allowed = models.BooleanField()

    def __str__(self):
        return self.book.name


# 3 Разработать набор моделей, для сайта-блога, на котором можно выставлять свои статьи, комментировать чужие, ставить
# лайк и дизлайк статье, и комментарию.
# 3.1 Доделать так, что бы связи позволяли комментировать комментарии.
# 3.2* Сделать лайки через GenericForeignKey

# class ArtcUser(models.Model):
#     name = models.CharField(max_length=100, blank=False)
#
#     def __str__(self):
#         return self.name
#
#
# class ArtcArticle(models.Model):
#     date = models.DateField(auto_now=True)
#     date_update = models.DateTimeField(auto_now_add=True)
#     header = models.CharField(max_length=100)
#     author = models.ForeignKey(ArtcUser, on_delete=models.CASCADE)
#     text = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.header
#
#
# class ArtcLikes(models.Model):
#     article = models.ForeignKey(ArtcArticle, on_delete=models.CASCADE)
#     user = models.ForeignKey(ArtcUser, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     like_dislike = models.BooleanField()
#
#     # class Meta:
#     #     unique_together = ['article', 'user']
#
#     def __str__(self):
#         return self.article.header
#
#
# class ArtcComment(models.Model):
#     # parrent = models.ForeignKey(ArtcArticle, on_delete=models.CASCADE)#models.ForeignKey('myapp.ArtcComment', null=True, blank=False, on_delete=models.DO_NOTHING)
#     article = models.ForeignKey(ArtcArticle, on_delete=models.CASCADE)
#     user = models.ForeignKey(ArtcUser, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now=True)
#     date_update = models.DateTimeField(auto_now_add=True)
#     comment_text = models.CharField(max_length=1000)
#
#     # GenericForeignKey
#
#     def __str__(self):
#         return self.user.name
