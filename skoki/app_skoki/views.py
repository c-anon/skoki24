from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world(request) -> HttpResponse:
    return render(request, 'app_skoki/base.html')
