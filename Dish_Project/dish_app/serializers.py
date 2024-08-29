from rest_framework import serializers
from .models import Dish
 
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id','name','price','category']
        read_only_fields = ['id']

class DishDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = DishSerializer.Meta.fields+['image']
        read_only_fields = ['id']

class DishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id','image']
        read_only_fields = ['id']
        extra_kwargs = {'image' : {'required' : True}}