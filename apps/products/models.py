from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    def __str__(self):
        return '%s %s %s %s %s %s' %(self.name, self.desc, self.weight, self.price, self.cost, self.category)