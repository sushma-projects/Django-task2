from django.db import models

class CsvFile(models.Model):
    carat = models.CharField(max_length=100)
    cut = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    clarity = models.CharField(max_length=100)
    depth = models.CharField(max_length=100)
    table = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    x = models.CharField(max_length=100)
    y = models.CharField(max_length=100)
    z = models.CharField(max_length=100)

    def __str__(self):
       return f'{self.carat} {self.cut} {self.color} {self.clarity} {self.depth} {self.table} {self.price} {self.x} {self.y} {self.z}'
