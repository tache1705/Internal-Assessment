from django.db import models
from django.http import HttpResponse


class Business(models.Model):
    title = models.TextField()
    description = models.TextField(default="It's some business data!")
    yearlyincome = models.FloatField()
    yearlyexpenses = models.FloatField()
    yearlyprofit = models.FloatField()
    initialinvest = models.FloatField()
    priceperserv = models.FloatField()

