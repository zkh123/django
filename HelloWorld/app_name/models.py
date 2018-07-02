# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.  https://linux.cn/article-9154-1.html
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ManyToManyField(Author, related_name="posts")

    def __str__(self):
        return self.title
