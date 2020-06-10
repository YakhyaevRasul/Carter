from rest_framework.serializers import ModelSerializer, SerializerMethodField
from restaurant.models import Restaurant, Food


class RestaurantListSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'location')
        model = Restaurant


class RestaurantSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Restaurant


class FoodListSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'price', 'picture')
        model = Food


class FoodSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Food


class RestaurantFoodSerializer(ModelSerializer):
    allfood = SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'allfood', 'location')

    def get_allfood(self, obj):
        serialized = FoodSerializer(obj.all_food, many=True)
        return serialized.data
