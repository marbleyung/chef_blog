from django.db.models import Q, Count
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import *
from .forms import CommentForm


class HomeView(generic.ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().select_related('category', 'author').order_by('-id')


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.\
            filter(category__slug=self.kwargs.get('slug')). \
            select_related('category', 'author').order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        posts = Post.objects.\
            filter(category__slug=self.kwargs.get('slug')). \
            select_related('category', 'author')\
            .annotate(number_of_comments=Count('comments'))

        category = Category.objects.get(slug=self.kwargs['slug'])
        context = {'category': category, 'posts': posts}
        return context


class AllPostsView(generic.ListView):
    model = Post
    context_object_name = 'all_posts'
    template_name = 'blog/all_posts.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.\
            all().select_related('category', 'author').order_by('-id')\
            .annotate(number_of_comments=Count('comments'))


class PostDetailView(generic.DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.\
            filter(slug=self.kwargs.get('post_slug')).prefetch_related('tags', 'comments').\
            select_related('author', 'category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_slug = self.kwargs.get('post_slug')
        post_pk = Post.objects.get(slug=post_slug).pk
        other_posts = Post.objects.filter(Q(pk=post_pk-1)|Q(pk=post_pk+1))\
            .select_related('category')
        context['other_posts'] = other_posts
        print(other_posts)
        context['form'] = CommentForm()
        return context


class CreateComment(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'blog/search_results.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        query = self.request.GET.get("q")
        posts = Post.objects.filter(Q(title__icontains=query) |
                                    Q(category__name__icontains=query))\
            .select_related('category', 'author').order_by('-id')\
            .annotate(number_of_comments=Count('comments'))
        context = {'query': self.request.GET.get('q'),
                   'posts': posts}
        return context

