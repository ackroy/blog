from django.shortcuts import render
from blog.models import Article, Tag, Classification
from django.template import RequestContext, loader
from django.http import HttpResponse
from django import template


def article_list(request):
    # latest_article_list = Article.objects.order_by('-publish_time')[:5]
    # template = loader.get_template('blog/index.html')
    latest_article_list = Article.objects.all()
    context = RequestContext(request, {
        'latest_article_list': latest_article_list,
    })
    return render(request, 'blog_list.html', context)


