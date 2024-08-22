from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class dish_model(models.Model):
    dish_name=models.CharField(max_length=50)

class Address(models.Model):
    city = models.CharField(max_length=20)
    postal_code = models.IntegerField()
    street_no = models.IntegerField()

class chef(models.Model):
    first_name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE,null = True)

class dish(models.Model):
    dish_name=models.CharField(max_length=50)
    price=models.IntegerField()
    rating = models.IntegerField(validators=[
        MinValueValidator(1),MaxValueValidator(5)
        ])
    chef = models.ForeignKey(chef,on_delete=models.CASCADE,null=True)

