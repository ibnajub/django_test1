from django.db import models
from django.contrib.auth.models import User


# from django.utils import timezone
# from django.utils.translation import gettext as _


class Topic(models.Model):
    author = models.ManyToManyField(User, )
    
    title = models.CharField(max_length=200, blank=False, null=True)
    description = models.TextField(max_length=10000, null=True)
    
    def __str__(self):
        return self.title


class Blogpost(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, )
    topic = models.ManyToManyField(Topic, )
    
    slug = models.SlugField(max_length=50, null=True)
    title = models.CharField(max_length=200, blank=False, null=True)
    content = models.TextField(max_length=10000, null=True)
    # created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "author - {}, topic - {}, id - {}".format(self.author.username, self.topic, self.id)


class Comment(models.Model):
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE, null=False, )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=10000, null=True)
    
    def __str__(self):
        return "{} by {}".format(self.id, self.author.username)
