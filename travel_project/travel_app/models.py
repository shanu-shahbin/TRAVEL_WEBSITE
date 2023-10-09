from django.db import models


# Create your models here.

class Place(models.Model):
    place_name = models.CharField(max_length=50)
    place_image = models.ImageField(upload_to='images')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.place_name
