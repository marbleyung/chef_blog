from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField(null=True, blank=True)
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class ContactLink(models.Model):
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=50, null=True)
    text = RichTextField()
    mini_text = RichTextField()

    def __str__(self):
        return self.name


class AboutImage(models.Model):
    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(About, on_delete=models.CASCADE,
                             related_name='images')
    alt = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.pk)


class Social(models.Model):
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name
