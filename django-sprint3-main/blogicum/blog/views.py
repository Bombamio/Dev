from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

import datetime


TODAY = datetime.date.today()
POST = Post.objects.select_related(
    'category', 'location', 'author',
).filter(
    is_published=True,
    category__is_published=True,
    pub_date__lte=TODAY,
)


def index(request):

    context = {
        'post_list': POST[:5],
    }

    return render(request, 'blog/index.html', context)


def post_detail(request, pk):

    post = get_object_or_404(
        POST,
        pk=pk
    )

    context = {
        'post': post,
    }

    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )

    post_list = Post.objects.select_related(
        'category', 'location', 'author',
    ).filter(
        category=category,
        is_published=True,
        pub_date__lte=TODAY,
    )

    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, 'blog/category.html', context)
