from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=20)
    place_name = models.CharField(max_length=30)
    details = models.TextField()
    image = models.ImageField(upload_to='name/place')

    def __str__(self):
        return self.name
