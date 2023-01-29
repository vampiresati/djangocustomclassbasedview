from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView

from .forms import MyAuthenticationForm

class MyLoginView(LoginView):   
    authentication_form = MyAuthenticationForm
    template_name="myapp/login.html"
class MyLogoutView(LogoutView):   
    template_name="myapp/logout.html"
class MyPasswordChangeView(PasswordChangeView):
    template_name="myapp/password_change.html"
    success_url='/myapp/passwordchangedone/'
class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name="myapp/passwordchangedone.html"

