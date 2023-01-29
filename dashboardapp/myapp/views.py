from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from django.contrib.auth.views import LoginView
def hello(request):
    return HttpResponse('hi how are oy')
def profile(request):
    return render(request,'registration/profile.html')
