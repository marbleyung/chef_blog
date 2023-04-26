from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

app_name = 'blog'

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', cache_page(60 * 60 * 24)(HomeView.as_view()), name='home'),
    path('p/posts/', AllPostsView.as_view(), name='all_posts'),
    path("search/", SearchResultsView.as_view(), name="search"),
    path('<slug:slug>/', PostListView.as_view(), name='posts'),
    path('comment/<int:pk>/', CreateComment.as_view(), name='create_comment'),
    path('<slug:slug>/<slug:post_slug>', PostDetailView.as_view(), name='post'),
]
