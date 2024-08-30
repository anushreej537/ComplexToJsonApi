from django.db import models

class Cafe(models.Model):
    item_name = models.CharField(max_length = 300)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.item_name