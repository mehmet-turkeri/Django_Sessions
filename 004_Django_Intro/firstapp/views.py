from django.shortcuts import render,HttpResponse # HttpResponse'u biz ekledik.

# Gorevi yerine getirecek kodlarimizi buraya yaziyoruz
def home(request):
    return HttpResponse('<h1>hello</h1>')

def about(request):
    return HttpResponse('<h1>About Sayfasina Hosgeldiniz.</h1>')
