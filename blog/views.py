from django.shortcuts import get_object_or_404, render
from blog.models import Article, Classification
from django.template import RequestContext
from django.db.models import Count


def article_list(request):
    latest_article_list = Article.objects.all()
    blog_in_classification = Classification.objects.annotate(class_count=Count('article')).order_by('-class_count')
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


def class_detail(request, class_id):
    # find all the articles whose classification id=class_id
    detail = Article.objects.filter(classification__id=class_id)
    context = RequestContext(request, {
        'detail': detail,
    })
    return render(request, 'class_detail.html', context)
