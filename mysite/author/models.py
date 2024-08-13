from django.db import models # type: ignore
from django.core.validators import MinValueValidator,MaxValueValidator # type: ignore
# Create your models here.
class author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MaxValueValidator(60),MinValueValidator(20)])
    city = models.CharField(max_length=100,null=True)
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),MinValueValidator(2)
    ],null=True)

    def __str__(self):
        return f' {self.first_name}  {self.last_name} {self.age} {self.city} {self.rating} '
 