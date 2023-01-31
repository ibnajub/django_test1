from django.contrib import admin
# from .models import Article
import models

admin.site.register(models.Catalog_author)
admin.site.register(models.Catalog_book)

admin.site.register(models.Library_author)
admin.site.register(models.Library_book)
admin.site.register(models.Library_book_Library_author)
admin.site.register(models.Library_User_reader)
admin.site.register(models.Library_user_reader_history)
admin.site.register(models.Library_allowed_book)

admin.site.register(models.Artc_user)
admin.site.register(models.Artc_article)
admin.site.register(models.Artc_likes)
admin.site.register(models.Artc_comment)