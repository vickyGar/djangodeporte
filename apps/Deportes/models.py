from django.db import models

# Create your models here.

class garment(models.Model):
    pk_id_garment = models.AutoField(primary_key=True, null=False, blank=False)
    mark = models.CharField(max_length=50, null=False, blank=False)
    size = models.DateField(auto_now=False, auto_now_add=True, null=False, blank=False)
    shop = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(null=False, blank=False, max_digits=3, decimal_places=2)
    discount = models.DecimalField(null=False, blank=False, max_digits=3, decimal_places=2)
    amount = models.IntegerField(null=False, blank=False)

class mark(models.Model):
    pk_id_mark = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
