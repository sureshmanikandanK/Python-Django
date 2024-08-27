from rest_framework import serializers
from .models import Author
 
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','city','age']
        read_only_fields = ['id']