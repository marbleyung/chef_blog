from django import template
from ..models import *


register = template.Library()


@register.simple_tag()
def get_social_links():
    return Social.objects.all()


@register.simple_tag()
def get_about():
    return About.objects.last()
