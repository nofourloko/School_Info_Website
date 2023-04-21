from django.urls import path
from . import views
urlpatterns = [
    path("", views.main_page, name='main_url'),
    path("allposts/", views.allposts, name='posts_url'),
    path("allposts/<slug:slug>", views.single_page, name="deatil_page"),
    path("form", views.create_post, name='form_url'),
    path("login", views.loginPage, name='login_url'),
    path("register", views.registerPage, name = "register_url"),
    path("logout", views.logout, name = "logout_url"),
    path("chat", views.chat, name = "chat_url"),
]
