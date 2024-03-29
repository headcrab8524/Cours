# Generated by Django 5.0.2 on 2024-02-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helicopter', '0005_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
