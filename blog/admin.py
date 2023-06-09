from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'id', )
    prepopulated_fields = {'slug': ('title', )}


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prep_time', 'cook_time', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)

