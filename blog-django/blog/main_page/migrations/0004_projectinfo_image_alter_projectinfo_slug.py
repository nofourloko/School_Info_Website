# Generated by Django 4.1.7 on 2023-04-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_projectinfo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False),
        ),
    ]
