from django.shortcuts import render
from django.http import HttpResponse

def homeview(request):
    return HttpResponse("Welcome BackEnd")
    # database den veriyi burda cekiyoruz.
