from django.contrib import admin

# admin panelde goruntuleyebilmek icin asagidakileri biz ekledik.
from .models import Student
admin.site.register(Student)
