from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello to HomePage.')


def myapp(request):
    return HttpResponse('Hello to Myapp Page.')


def welcome(request):
    return HttpResponse('Hello to Myapp/WelcomePage.')

