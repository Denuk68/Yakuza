from django.db import models
from datetime import datetime


class Pizza(models.Model):
    name = models.CharField("Назва страви", max_length=50)
    price = models.IntegerField("Ціна страви")
    description = models.TextField("Опис страви", max_length=250)
    image = models.ImageField(upload_to='Pizza/%Y/%m/%d/')
    

    def __str__(self):
        return self.name

    class Meta:        
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizza'


class Sushi(models.Model):
    name = models.CharField("Назва страви", max_length=50)
    price = models.IntegerField("Ціна страви")
    description = models.TextField("Опис страви", max_length=250)
    image = models.ImageField(upload_to='Sushi/%Y/%m/%d/')
   
    

    def __str__(self):
        return self.name

    class Meta:        
        verbose_name = 'Sushi'
        verbose_name_plural = 'Sushi'


class Dessert(models.Model):
    name = models.CharField("Назва страви", max_length=50)
    price = models.IntegerField("Ціна страви")
    description = models.TextField("Опис страви", max_length=250)
    image = models.ImageField(upload_to='Dessert/%Y/%m/%d/')
    

    def __str__(self):
        return self.name

    class Meta:        
        verbose_name = 'Dessert'
        verbose_name_plural = 'Dessert'


class New(models.Model):
    name = models.CharField("Назва страви", max_length=50)
    price = models.IntegerField("Ціна страви")
    description = models.TextField("Опис страви", max_length=250)
    image = models.ImageField(upload_to='New/%Y/%m/%d/')
    

    def __str__(self):
        return self.name

    class Meta:        
        verbose_name = '1. New Dishes'
        verbose_name_plural = '1. New Dishes'
