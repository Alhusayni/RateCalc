from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Calculator(models.Model):
    isSup = (
        ('Yes', 'نعم'),
        ('No', 'لا')
    )
    Price = models.PositiveBigIntegerField()
    Salary = models.PositiveBigIntegerField()
    Years = models.PositiveBigIntegerField()
    DownPay = models.PositiveBigIntegerField()
    IntrestRate = models.FloatField()
    isSupported = models.CharField(max_length=100, choices=isSup, default='')
    timestamp = models.DateTimeField(default=timezone.now())


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)