from django.db import models

# Create your models here.
class Gun(models.Model):
  make = models.CharField(max_length=20)
  model = models.CharField(max_length=20)
  caliber = models.CharField(max_length=5)
  price = models.DecimalField(max_digits=10, decimal_places=2)