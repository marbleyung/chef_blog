from django.views import generic
from .models import *


class HomeView(generic.ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().select_related('category', 'author')


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.\
            filter(category__slug=self.kwargs.get('slug')). \
            select_related('category', 'author')


class PostDetailView(generic.DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.\
            filter(slug=self.kwargs.get('post_slug'))
