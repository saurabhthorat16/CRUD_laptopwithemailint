from django.db import models

# Create your models here.
class Laptop(models.Model):
    lid = models.IntegerField()
    brand_name = models.CharField(max_length=40)
    model_name = models.CharField(max_length=40)
    price = models.IntegerField()
    rom = models.CharField(max_length=40)
    ram = models.CharField(max_length=40)
    SSD = models.CharField(max_length=40)
    HDD = models.CharField(max_length=40)
    Weight = models.FloatField()
    year = models.IntegerField()

    def __str__(self):
        return f'{self.lid}-{self.brand_name}-{self.model_name}-{self.price}-{self.rom}-{self.ram}-{self.SSD}-{self.HDD}-{self.Weight}-{self.year}'
