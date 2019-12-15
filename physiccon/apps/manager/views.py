from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import User


def index(request):
    return render(request, 'physics-con/index.html')


def test(request):
    usr = User(user_name=request.GET['name'], user_email=request.GET['email'], user_phone=request.GET['subject'])
    usr.save()
    return render(request, 'ContactFrom_v1/index.html')
