from django.contrib import admin
# from .models import Article
# from myapp import models
from .models import CatalogAuthor, CatalogBook, LibraryAuthor, LibraryBook, LibraryUserReader, LibraryUserReaderHistory\
    ,LibraryAllowedBook, ArtcArticle, ArtcLikes, ArtcComment, ArtcUser



admin.site.register(CatalogAuthor)
admin.site.register(CatalogBook)

admin.site.register(LibraryAuthor)
admin.site.register(LibraryBook)
admin.site.register(LibraryUserReader)
admin.site.register(LibraryUserReaderHistory)
admin.site.register(LibraryAllowedBook)


admin.site.register(ArtcUser)
admin.site.register(ArtcArticle)
admin.site.register(ArtcLikes)
admin.site.register(ArtcComment)