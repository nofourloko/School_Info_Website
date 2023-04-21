from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class ProjectInfo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    tech = models.TextField()
    image = models.ImageField(upload_to="images")
    slug = models.SlugField(default="", null=False, blank=True, editable=False)

    def get_absolute_url(self):
        return reverse("detail_page", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Chat(models.Model):
    user = models.CharField(max_length=50)
    message = models.CharField(max_length=500)