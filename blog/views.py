from django.shortcuts import get_object_or_404, render
from blog.models import Article, Classification
from django.template import RequestContext, loader
from django.http import HttpResponse
from django import template


def article_list(request):
    # latest_article_list = Article.objects.order_by('-publish_time')[:5]
    # template = loader.get_template('blog/index.html')
    latest_article_list = Article.objects.all()
    blog_in_classification = Classification.objects.all()
    context = RequestContext(request, {
        'latest_article_list': latest_article_list,
        'blog_in_classification': blog_in_classification,
    })
    return render(request, 'blog_list.html', context)


def artical_detail(request, blog_id):
    blog_detail = get_object_or_404(Article, pk=blog_id)
    context = RequestContext(request, {
        'blog_detail': blog_detail,
    })
    return render(request, 'blog_detail.html', context)



