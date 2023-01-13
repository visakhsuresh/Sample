from django.db import models

# Create your models here.
class Rating(models.Model):
    name=models.CharField(max_length=2000)
    price=models.FloatField()
    image=models.CharField(max_length=5000)
    stock=models.IntegerField()