from django.db import models
from datetime import datetime


class Food(models.Model):
    name = models.CharField("Назва страви", max_length=50)
    price = models.IntegerField("Ціна страви")
    description = models.TextField("Опис страви", max_length=250)
    image = models.ImageField(upload_to='food/%Y/%m/%d/')
    food_type = models.CharField("Тип страви",  max_length=50)

    def __str__(self):
        return self.name
