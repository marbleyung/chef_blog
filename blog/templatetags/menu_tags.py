from django import template
from ..models import Category, Post

register = template.Library()


def get_all_categories():
    return Category.objects.all()


@register.simple_tag()
def get_list_categories():
    return get_all_categories()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    categories = get_all_categories()
    return {'categories': categories}


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_last_posts(count=5):
    last_posts = Post.objects.all().select_related('category').order_by('-id')[:5]
    return {'last_posts': last_posts}
