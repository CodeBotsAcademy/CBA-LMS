from django.db import models

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='media/')