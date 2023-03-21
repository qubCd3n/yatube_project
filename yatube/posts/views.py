from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Group, Post, User

POSTS_PER_PAGE = 10


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    
    return render(request, template, context,)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context, slug)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)
    paginator = Paginator(author.posts.all(), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'posts': posts,
        'page_number': page_number,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    one_post = get_object_or_404(Post, id=post_id)
    context = {
        'one_post': one_post,
        'post_title': one_post.text,
    }
    return render(request, 'posts/post_detail.html', context)