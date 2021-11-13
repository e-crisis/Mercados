from django.db import models

# Create your models here.

class Transport(models.Model):
    car_name = models.CharField(max_length=30)
    yr_mfr = models.IntegerField()
    date_mfr = models.DateField()
    fuel_type = models.CharField(max_length=30, null=True)
    kms_run = models.IntegerField()
    sale_price = models.IntegerField()
    city = models.CharField(max_length=30, null=True)
    times_viewed = models.IntegerField()
    body_type = models.CharField(max_length=30, null=True)
    transmission = models.CharField(max_length=30, null=True)
    variant = models.CharField(max_length=100, null=True)
    assured_buy = models.BooleanField(max_length=30)
    emi_starts_from = models.IntegerField()
    booking_down_pymnt = models.IntegerField()
    total_owners = models.IntegerField()