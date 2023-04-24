from django.shortcuts import render
from django.views import generic
from .models import *


def home(request):
    return render(request, 'base.html')


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.\
            filter(category__slug=self.kwargs.get('slug')). \
            select_related('category')


class PostDetailView(generic.DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.\
            filter(slug=self.kwargs.get('post_slug')). \
            select_related('category').prefetch_related('recipes')
