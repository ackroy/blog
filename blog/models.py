from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField


class Blogtype(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    blogtype = models.ForeignKey(Blogtype)
    content = RichTextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        ordering = ['-publish_time']

# class Comment(models.Model):
#     blog = models.ForeignKey(Blog)
#     name = models.CharField(max_length=16)
#     email = models.EmailField()
#     content = RichTextField()
#     created_time = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.title

class Archive(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.title