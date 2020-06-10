from django.contrib import admin

from restaurant.models import Restaurant, Food

admin.site.register(Restaurant)
admin.site.register(Food)