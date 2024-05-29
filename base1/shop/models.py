from django.db import models
from django.utils import timezone



class Category(models.Model):
    title= models.CharField(max_length=255)  #длина названия
    created_at = models.DateTimeField(default=timezone.now) #когда создан
    def __str__(self):
        return self.title




class Course(models.Model):
    title= models.CharField(max_length=300) #длина названия
    price = models.FloatField() #цена в float формате,с плавающей точкой
    students_qty = models.IntegerField() #кол-во студентов в формате int
    reviews_qty = models.IntegerField() #кол-во отзывов в формате int
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #при удалении категории удаляются все курсы этой категории
    created_at = models.DateTimeField(default=timezone.now) #когда создан
    def __str__(self):
        return self.title
