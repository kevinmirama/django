from django.db import models

class Contacto(models.Model):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)

