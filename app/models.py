from django.db import models

# Create your models here.
class Name(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    course=models.CharField(max_length=100)

    def __str__(self):
        return self.name