from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from restaurant.serializers import (
    RestaurantListSerializer,
    RestaurantFoodSerializer,
    RestaurantSerializer,
    FoodListSerializer,
    FoodSerializer,
)
from restaurant.models import Restaurant, Food


class RestaurantModelViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action == "list":
            return RestaurantListSerializer
        return RestaurantSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class RestaurantFoodAPIView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = RestaurantFoodSerializer

    def get(self, request, *args, **kwargs):
        rest = self.get_object()
        serialized = RestaurantFoodSerializer(rest)
        return Response(serialized.data)


class FoodModelViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action == "list":
            return FoodListSerializer
        return FoodSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
