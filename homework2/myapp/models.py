from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# from django.utils import timezone
# from django.utils.translation import gettext as _


class Topic(models.Model):
    author = models.ManyToManyField(User, related_name='authors')
    
    title = models.CharField(max_length=200, blank=False, null=True)
    description = models.TextField(max_length=10000, null=True)
    
    def __str__(self):
        return self.title


class Blogpost(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='blog_authors')
    topic = models.ManyToManyField(Topic, related_name='topics')
    
    slug = models.SlugField(max_length=50, null=True, unique=True, db_index=True)
    title = models.CharField(max_length=200, blank=False, null=True)
    content = models.TextField(max_length=10000, null=True)
    # created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super().save(**kwargs)
    
    def __str__(self):
        return "Author: {}; Title: {}; Slug: {}".format(self.author.username, self.title, self.slug)


class Comment(models.Model):
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE, null=False, related_name='blogs')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comment_authors')
    
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=10000, null=True)
    
    def __str__(self):
        return "{} by {}".format(self.id, self.author.username)
