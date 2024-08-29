from django.db import models
from category_app.models import categorymodel
# Create your models here.

def dish_image_path(instance,filename):
    return '/'.join(['uploads',str(instance.name),filename])

class Dish(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image = models.ImageField(upload_to=dish_image_path,null=True,blank=True)
    category = models.ForeignKey(categorymodel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name