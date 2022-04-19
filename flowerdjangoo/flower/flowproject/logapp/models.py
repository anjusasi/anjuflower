from django.db import models

# Create your models here.
class Flower(models.Model):
    customername = models.CharField(max_length=230)
    phonenumber = models.CharField(max_length=250)
    email = models.EmailField()
    address = models.TextField()
    quantity = models.IntegerField()
    city = models.CharField(max_length=120)
    item = models.CharField(max_length=120)
    district = models.CharField(max_length=120)

    def __str__(self):
        return self.customername
