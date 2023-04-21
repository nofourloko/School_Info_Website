from django.contrib import admin

# Register your models here.
from .models import ProjectInfo,Users,Chat

admin.site.register(ProjectInfo)
admin.site.register(Users)
admin.site.register(Chat)