from rest_framework import serializers
from .models import categorymodel
from dish_app.serializers import DishSerializer

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.IntegerField(write_only = True)
    category_id = DishSerializer(read_only = True)
    class Meta:
        model = categorymodel
        fields = ['id','category_name','category_id']
        read_only_fields=['id']