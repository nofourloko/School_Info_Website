from django.shortcuts import redirect, render
from django.urls import reverse
from .models import ProjectInfo, Users, Chat
from django.views.generic.edit import FormView
from .forms import PostForm,LoginForm,ChatForm
from django.http import HttpResponseRedirect
# Create your views here.
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allposts")
    else:
        form = PostForm()
    return render(request, 'main_page/form.html', {'form': form})

def main_page(request):
    data = ProjectInfo.objects.last()
    return render(request, "main_page/main_page.html", {"info" : data})

def allposts(request):
    data = ProjectInfo.objects.all()    
    return render(request, "main_page/allposts.html", {"info" : data})

def single_page(request, slug):
    page = ProjectInfo.objects.get(slug=slug)
    return render(request, "main_page/single_page.html" , {"info" : page})

def loginPage(request):
    form = LoginForm()
    if request.session["is_logged"] is False:
        if request.method == 'POST':
            m = Users.objects.get(username = request.POST['username'])
            if m :
                if m.password == request.POST['password']:
                    request.session["is_logged"] = True
                    request.session["current_user"] = m.username
                    return HttpResponseRedirect("/")
                else:
                    return render(request, 'main_page/login.html', {'form': form, "text" : "nie ma takiego hasła "})   
            else:
                return render(request, 'main_page/login.html', {'form': form, "text" : "nie ma takiego loginu "})   
        else:      
            return render(request, 'main_page/login.html', {'form': form})   
    return HttpResponseRedirect("/")
def registerPage(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                form.save()     
                return HttpResponseRedirect("login")
        else:  
            form = LoginForm()
            return render(request, 'main_page/register.html', {'form': form})

def logout(request):
    request.session["is_logged"] = False
    return HttpResponseRedirect("/")

def chat(request):
    current_user = request.session["current_user"]
    if request.session["is_logged"] is False:
       return render(request, 'main_page/login_redirect.html')
    else:
        if request.method == "POST":
            message = request.POST.get("message", "")
            new_message = Chat(user=current_user, message=message)
            form = ChatForm(request.POST, instance=new_message)
            if form.is_valid():
                form.save()     
                return HttpResponseRedirect("chat")
        form = ChatForm()
        messages = Chat.objects.all()
        return render(request, 'main_page/chat.html', {
            "form" : form,
            "messages" : messages
            })