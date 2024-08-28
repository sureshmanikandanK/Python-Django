from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from author_app.models import Author


# Create your models here.
class bookmodel(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),MinValueValidator(1)
        ]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        
