from django.db import models


class Product(models.Model):  #models.Model : Map your Python class to a database table
    name=models.CharField(max_length=255) #setting the name to be a textual data of max length 255
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)

class Offer(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()


