from django.contrib import admin
# from .models import Article
import models

admin.site.register(models.Author1)
admin.site.register(models.Book1)

admin.site.register(models.Author2)
admin.site.register(models.Book2)
admin.site.register(models.User_reader)
admin.site.register(models.User_reader_history)
admin.site.register(models.allowed_books)

admin.site.register(models.User)
admin.site.register(models.Article)
admin.site.register(models.Likes)
admin.site.register(models.Comment)