from rest_framework import serializers
from .models import categorymodel
from dish_app.serializers import DishSerializer

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(write_only = True)
    class Meta:
        model = categorymodel
        fields = ['id','category_name']
        read_only_fields=['id']