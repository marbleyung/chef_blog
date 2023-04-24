from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('<slug:slug>/', PostListView.as_view(), name='posts'),
    path('<slug:slug>/<slug:post_slug>', PostDetailView.as_view(), name='post'),
    path('', home, name='home'),
]
