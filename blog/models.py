from __future__ import unicode_literals
from django.db import models


# class Tag(models.Model):
#     tag_name = models.CharField(max_length=10)
#     create_time = models.DateTimeField(auto_now_add=True)
#
#     def __unicode__(self):
#         return self.tag_name


class Category(models.Model):
    name = models.CharField(max_length=20)
    # article_num = models.IntegerField()

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    # author = models.ForeignKey(Author)
    # tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    name = models.CharField(max_length=16)
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)


