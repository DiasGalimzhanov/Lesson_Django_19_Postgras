from django.db import models
from django.contrib.postgres import fields

class Phones(models.Model):
    name = fields.ArrayField(models.CharField(max_length=20),size=2)
    description = models.TextField()
    date_range = fields.DateRangeField()
    price = fields.IntegerRangeField()

    def __str__(self):
        return f"{self.name[0]} {self.name[1]}"