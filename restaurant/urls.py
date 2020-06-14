from django.urls import path, include
from rest_framework import routers
from restaurant.views import (
    RestaurantModelViewSet,
    FoodModelViewSet,
    RestaurantFoodAPIView,
    RestaurantFoodRetrieveAPIView)

router = routers.SimpleRouter()
router.register('restaurants', RestaurantModelViewSet)
router.register('food', FoodModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('recipe/', RestaurantFoodAPIView.as_view()),
    path('recipe/<int:pk>/', RestaurantFoodRetrieveAPIView.as_view()),
]
