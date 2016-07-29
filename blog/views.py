from django.shortcuts import get_object_or_404, render
from blog.models import Blog, Category
from django.template import RequestContext
from django.db.models import Count
from django.conf import settings


def index(request):
    latest_blog_list = Blog.objects.all()
    blog_in_cat = Category.objects.annotate(cat_counter=Count('blog')).order_by('-cat_counter')
    context = RequestContext(request, {
        'latest_blog_list': latest_blog_list,
        'blog_in_cat': blog_in_cat,
    })
    return render(request, 'index.html', context)


def blog_detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    detail.content = detail.content.decode('utf8')
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


def test(request):
    context = RequestContext(request, {
        # 'base_dir': settings.BASE_DIR,
        # 'static_URL': settings.STATIC_URL,
        # 'static_dir': settings.STATIC_ROOT,
        # 'staticfiles_dir': settings.STATICFILES_DIRS,
    })
    return render(request, 'test.html', context)


def blog_index(request):
    context = RequestContext(request, {

    })
    return render(request, 'index.html', context)
