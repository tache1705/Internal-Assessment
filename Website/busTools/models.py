from django.db import models
from django.http import HttpResponse


class BreakEven(models.Model):
    busName = models.TextField()
    units = models.FloatField()
    fixCost = models.FloatField()
    pricePUnit = models.FloatField()
    variable = models.FloatField()


class Decision(models.Model):
    busName = models.TextField()

    decison1 = models.TextField()
    probability1 = models.FloatField()
    cost1 = models.FloatField()
    profitFail1 = models.FloatField
    profitSuccess1 = models.FloatField

    decison2 = models.TextField()
    probability2 = models.FloatField()
    cost2 = models.FloatField()
    profitFail2 = models.FloatField
    profitSuccess2 = models.FloatField

    decison3 = models.TextField()
    probability3 = models.FloatField()
    cost3 = models.FloatField()
    profitFail3 = models.FloatField
    profitSuccess3 = models.FloatField


class ForceField(models.Model):
    busName = models.TextField()

    proLevel4 = models.TextField(blank=True)
    proLevel3 = models.TextField(blank=True)
    proLevel2 = models.TextField(blank=True)
    proLevel1 = models.TextField(blank=True)

    conLevel4 = models.TextField(blank=True)
    conLevel3 = models.TextField(blank=True)
    conLevel2 = models.TextField(blank=True)
    conLevel1 = models.TextField(blank=True)

    def __str__(self):
        return self.busName


class Graphing(models.Model):
    busName = models.TextField()

    yVarName = models.TextField()
    xVarName = models.TextField()
    function = models.TextField()
