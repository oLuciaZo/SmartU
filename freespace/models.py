from django.db import models

# Create your models here.
from django.db.models.fields import CharField

class Capacity(models.Model):
    building = models.CharField(max_length=50)
    ap = models.IntegerField(default=0)
    client = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.building} - {self.ap} - {self.client}'
    def percentage(self):
        return int((self.client/(self.ap * 30)) * 100)
    def condition(self):
        if int((self.client/(self.ap * 30)) * 100) < 65:
            return "Recomend you to Study Online in This Building"
        elif int((self.client/(self.ap * 30)) * 100) < 75:
            return "Concurrent Users are Density may caused The Online Study"
        elif int((self.client/(self.ap * 30)) * 100) > 75:
            return "Concurrent Users too Fucking JAM RunAway"

