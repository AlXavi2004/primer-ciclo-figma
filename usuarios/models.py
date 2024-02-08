from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(verbose_name = 'email', max_length=255, unique = True)
    password = models.CharField(max_length=255)

