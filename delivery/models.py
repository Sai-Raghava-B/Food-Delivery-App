# delivery/models.py
from django.db import models

class Organization(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    TYPE_CHOICES = (
        ('perishable', 'Perishable'),
        ('non-perishable', 'Non-Perishable'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    # type = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    base_distance = models.DecimalField(max_digits=6, decimal_places=2)
    per_km_price_perishable = models.DecimalField(max_digits=6, decimal_places=2)
    per_km_price_non_perishable = models.DecimalField(max_digits=6, decimal_places=2)
