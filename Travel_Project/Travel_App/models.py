from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=22)
    decri = models.TextField()
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=15)
    decri = models.TextField()
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
