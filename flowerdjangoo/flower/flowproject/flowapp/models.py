from django.db import models

# Create your models here.
class Front(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    des = models.TextField()
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
