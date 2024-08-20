from django.db import models

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=20)
    text = models.CharField(max_length=20)
    rating = models.IntegerField(max_length=20)

