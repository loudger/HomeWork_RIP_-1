from django.db import models
from django.contrib.auth.models import AbstractUser


class Car(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    brand = models.CharField(max_length=100, blank=True, verbose_name='Марка')
    year = models.IntegerField(blank=True, null=True, verbose_name='Год выпуска')
    mileage = models.CharField(max_length=100, blank=True, verbose_name='Пробег')
    gas = models.IntegerField(blank=True, null=True, verbose_name='Бензобак')
    image = models.FileField(upload_to='images/', null=True, blank=True,
                             default='images/default_car.jpg', verbose_name='Фотография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобиль'

class User(AbstractUser):
    favorite_brand = models.CharField(max_length=40, blank=True, verbose_name='Любимый бренд')
    about_me = models.TextField(max_length=1000, blank=True, verbose_name='О себе')
    cars = models.ManyToManyField(Car, blank=True)
    image = models.FileField(upload_to='avatars/', null=True, blank=True,
                             default='avatars/default_avatar.png', verbose_name='Аватар')




