from django.db import models

class Imagen(models.Model):
    image = models.ImageField(upload_to = 'media/')