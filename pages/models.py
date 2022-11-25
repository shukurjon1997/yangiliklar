from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    adminlar = (
        ("Shahzod","Shahzod"),
        ("Anvar", "Anvar"),
        ("Qobil", "Qobil"),
        ("Davron","Davron"),
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    summery = models.CharField(max_length=200)
    photo = models.ImageField(upload_to= 'images/')
    data = models.DateTimeField()
    admin = models.CharField(max_length = 10, choices= adminlar)
    
    def __str__(self):
        return self.title
class Murojaat(models.Model):
    ism = models.CharField(max_length=16)
    familya = models.CharField(max_length=25)
    tel = models.PositiveIntegerField(max_length=9)
    murojaat = models.TextField()
    vaqt = models.DateTimeField()
    
    def __str__(self):
        return self.murojaat

    def get_absolute_url(self):
        return reverse('contact')