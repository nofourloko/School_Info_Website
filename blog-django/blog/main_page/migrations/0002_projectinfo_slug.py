# Generated by Django 4.1.7 on 2023-04-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='slug',
            field=models.SlugField(default=10, unique=True),
            preserve_default=False,
        ),
    ]