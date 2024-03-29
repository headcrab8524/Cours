# Generated by Django 5.0.2 on 2024-02-20 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helicopter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='choper',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='helicopter.category'),
        ),
    ]
