from django.db import models

# Create your models here.


class Duck(models.Model):
    nombre = models.CharField(max_length=255)
    segundo_nombre = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    edad = models.IntegerField()

class UserDuck(models.Model):
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    ducks = models.ForeignKey(Duck,on_delete=models.CASCADE)
    