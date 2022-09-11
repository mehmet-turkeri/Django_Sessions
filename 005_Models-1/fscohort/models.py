from pyexpat import model
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    number = models.IntegerField()
    about = models.TextField()
    register_date = models.DateField(auto_now_add=True) # Ögrencinin kayıt tarihi. Sadece bir kere alacagı için - auto_now_add=True
    last_update = models.DateTimeField(auto_now=True) # Ögrenci bilgileri enson guncelleme tarihi. Her seferinde - auto_now=True
    is_active = models.BooleanField(default=True)    

# Date sadece tarihi gun ay yil seklinde alir. DateTime ise hem tarihi hemde saati alir. 

    def __str__(self): # Tablodaki kayitlarin istedigimiz formatta gozukmesi icin
        return f"{self.number} - {self.first_name}"

    
    class Meta: # Kayitlarin neye gore siralacagini belirler. Burda numbera gore siralanacak
        ordering = ["number"]
        verbose_name_plural = "Student_List"   
    
