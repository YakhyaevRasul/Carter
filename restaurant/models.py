from django.db import models
import uuid
import os

def get_food_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('media/', filename)


class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    picture = models.ImageField(upload_to=get_food_pic_path, null=True, blank=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='allfood')

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    @property
    def all_food(self):
        return self.allfood.all()

    def __str__(self):
        return self.name

