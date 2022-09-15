from django.db import models

# Dont forget: makemigrations
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()

# Burda bir model yazdım. Şimdi makemigrations komutuyla bunu Djangoya bildirecegim.

    # Bu listedeki kayitlarin istedigimiz formatta gorunmesini saglar. Girintiye dikkat edin
    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"

    # Buda siralamnin neye gore yapilacagini belirtir
    class Meta:
        ordering = ['number']   # for DESC -> '-number' yani ters siralamak isterseniz basina eksi koyun.
        verbose_name_plural = 'Öğrenciler' # Tablomuzun ismini degistirmek icin

