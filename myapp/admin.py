from django.contrib import admin
# from .models import Article
# import models
from .models import Catalog_book,Catalog_author,Library_book,Library_author,Library_user_reader_history,\
    Library_User_reader,Library_allowed_book,Artc_user,Artc_article,Artc_likes,Artc_comment

admin.site.register(Catalog_author)
admin.site.register(Catalog_book)
#
admin.site.register(Library_author)
admin.site.register(Library_book)

admin.site.register(Library_User_reader)
admin.site.register(Library_user_reader_history)
admin.site.register(Library_allowed_book)

admin.site.register(Artc_user)
admin.site.register(Artc_article)
admin.site.register(Artc_likes)
admin.site.register(Artc_comment)