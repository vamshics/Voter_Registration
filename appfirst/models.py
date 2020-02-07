from django.db import models

# Create your models here.
class Xyz(models.Model):
    nm=models.CharField(max_length=50),
    email=models.EmailField(),
    mbno=models.IntegerField(),


