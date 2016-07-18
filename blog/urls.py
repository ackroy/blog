from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='index'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.artical_detail, name='detail'),
]