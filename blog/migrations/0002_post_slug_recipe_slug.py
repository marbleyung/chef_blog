# Generated by Django 4.2 on 2023-04-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]