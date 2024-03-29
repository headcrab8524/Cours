# Generated by Django 5.0.2 on 2024-02-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helicopter', '0004_alter_choper_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
    ]