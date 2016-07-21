from django.shortcuts import get_object_or_404, render
from blog.models import Blog, Category
from django.template import RequestContext
from django.db.models import Count


def index(request):
    latest_blog_list = Blog.objects.all()
    blog_in_cat = Category.objects.annotate(cat_counter=Count('blog')).order_by('-cat_counter')
    context = RequestContext(request, {
        'latest_blog_list': latest_blog_list,
        'blog_in_cat': blog_in_cat,
    })
    return render(request, 'blog_list.html', context)


def blog_detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    context = RequestContext(request, {
        'blog_detail': detail,
    })
    return render(request, 'blog_detail.html', context)


def cat_detail(request, cat_id):
    # find all the articles whose classification id=class_id
    detail = Blog.objects.filter(category__id=cat_id)
    context = RequestContext(request, {
        'detail': detail,
    })
    return render(request, 'cat_detail.html', context)
