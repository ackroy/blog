#coding:utf-8

from django.shortcuts import get_object_or_404, render
from blog.models import Blog, Category, Profile, Archive, Blogtype
from django.template import RequestContext
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def _get_latest_objs(objs, latest_num=8):
    """
    get the latest 8 objs
    :param objs:
    :param latest_num:
    :return:
    """

    objs_num = objs.count()
    if objs_num < latest_num:
        latest_num = objs_num

    latest = []
    for obj in objs:
        latest.append({'title': obj.title, 'id':obj.id})

    return latest



def index(request):
    latest_blog_list = Blog.objects.all()

    latest_blogs = _get_latest_objs(latest_blog_list)


    # tags = Tag.objects.all()
    paginator = Paginator(latest_blog_list, 5)
    page = request.GET.get('page')
    try:
        latest_blog = paginator.page(page)
    except PageNotAnInteger:
        latest_blog = paginator.page(1)
    except EmptyPage:
        latest_blog = paginator.page(paginator.num_pages)

    blog_in_cat = Category.objects.annotate(cat_counter=Count('blog')).order_by('-cat_counter')

    context = RequestContext(request, {
        'latest_blog_list': latest_blog,
        'blog_in_cat': blog_in_cat,
        # 'tags': tags,
        'latest_blogs': latest_blogs
    })
    return render(request, 'index.html', context)


def blog_detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    # detail.content = detail.content.decode('utf8')
    context = RequestContext(request, {
        'blog': detail,
    })
    return render(request, 'detail.html', context)


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


def profile(request):
    profile_blog = Profile.objects.get(title='Profile')

    context = RequestContext(request, {
        'profile': profile_blog
    })
    return render(request, 'profile.html', context)


# def tag_page(request, tag_id):
#     get_tag = Tag.objects.get(id=tag_id)
#     detail = Blog.objects.filter(tags=get_tag)
#
#     context = RequestContext(request, {
#         'blogs': detail,
#         'get_tag': get_tag
#     })
#     return render(request, 'tag.html', context)

def about_site(request):
    archive = Archive.objects.get(title='Archive')

    context = RequestContext(request, {
        'archive': archive
    })
    return render(request, 'archive.html', context)


def _get_cat_blogs():
    blog_in_cat = Category.objects.annotate(cat_counter=Count('blog')).order_by('-cat_counter')
    return blog_in_cat


def tech(request):
    cat = Blogtype.objects.get(name='tech')
    cat_blog_list = Blog.objects.filter(blogtype=cat)
    tech_blogs = _get_latest_objs(cat_blog_list)

    blog_in_cat = _get_cat_blogs()
    paginator = Paginator(cat_blog_list, 5)
    page = request.GET.get('page')
    try:
        cat_blog = paginator.page(page)
    except PageNotAnInteger:
        cat_blog = paginator.page(1)
    except EmptyPage:
        cat_blog = paginator.page(paginator.num_pages)

    context = RequestContext(request, {
        'cat_blog': cat_blog,
        'tech_blogs': tech_blogs,
        'blog_in_cat': blog_in_cat
    })

    return render(request, 'tech.html', context)
#
#
def essay(request):
    cat = Blogtype.objects.get(name='essay')
    cat_blog_list  = Blog.objects.filter(blogtype=cat)
    essay_blogs = _get_latest_objs(cat_blog_list)

    blog_in_cat = _get_cat_blogs()

    paginator = Paginator(cat_blog_list, 5)
    page = request.GET.get('page')
    try:
        cat_blog = paginator.page(page)
    except PageNotAnInteger:
        cat_blog = paginator.page(1)
    except EmptyPage:
        cat_blog = paginator.page(paginator.num_pages)

    context = RequestContext(request, {
        'cat_blog': cat_blog,
        'essay_blogs': essay_blogs,
        'blog_in_cat': blog_in_cat
    })

    return render(request, 'essay.html', context)




