from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),

    # blog page
    url(r'^$', views.index, name='show_blog'),

    # detail of blog
    url(r'^(?P<blog_id>[0-9]+)/$', views.blog_detail, name='detail'),

    # show blog with same category
    url(r'^cat=(?P<cat_id>[0-9]+)/$', views.cat_detail, name='cat'),

    url(r'^test', views.test, name='test'),

    url(r'^index', views.blog_index, name='blog_index'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
