from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Изделие")
    height = models.IntegerField(verbose_name="Высота")
    width = models.IntegerField(verbose_name="Ширина")
    cost = models.IntegerField(verbose_name="Цена")
    pct = models.ImageField(upload_to="myappp/static/img",blank=True)

    def __str__(self):
        return self.name
    
class Shop(models.Model):
    name = models.CharField(max_length=10)
    cost = models.IntegerField
    proz = models.FloatField
    def check123(self, cost, proz):
        return cost*proz
#        return {self.cost}*{self.proz}

#test54654654s