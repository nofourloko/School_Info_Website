# Generated by Django 4.1.7 on 2023-04-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_alter_projectinfo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
