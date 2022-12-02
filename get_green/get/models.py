from django.db import models

# Create your models here.
class pro(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=10000)
    co_non=models.CharField(max_length=10)

class rank(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    