from django import forms
from .models import ProjectInfo, Users, Chat

class PostForm(forms.ModelForm):
    class Meta:
        model = ProjectInfo
        fields = "__all__"

        labels = {
            "title": "Tytul",
            "desc": "Twoj opis",
            "tech": "Przedmiot",
            "image": "Zdjecie"
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

        labels = {
            "username" : "Login",
            "password" : "Hasło"
        }

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ["message"]

        labels = {
            "message" : "Napisz swoja wiadomosc"
        }