from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name='children',
                               on_delete=models.SET_NULL,
                               null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, related_name='post',
                                 on_delete=models.SET_NULL,
                                 null=True)
    tags = models.ManyToManyField(Tag, related_name='post')
    author = models.ForeignKey(User, related_name='post',
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug': self.category.slug,
                                       'post_slug': self.slug})


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=100)
    prep_time = models.PositiveSmallIntegerField(default=0)
    cook_time = models.PositiveSmallIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(Post, related_name='recipes',
                             on_delete=models.SET_NULL,
                             null=True, blank=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comment',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name


