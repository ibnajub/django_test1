from django.contrib import admin

# Register your models here.


from .models import Topic, Comment, Blogpost

admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Blogpost)
