from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from .models import User


def index(request):
    return render(request, 'physics-con/index.html')


def test(request):
    try:
        usr = User(user_name=request.GET['name'], user_email=request.GET['email'], user_phone=request.GET['subject'])
        usr.save()
    except MultiValueDictKeyError:
        print("ok")
    return render(request, 'ContactFrom_v1/index.html')
