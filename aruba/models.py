from django.db import models
#from django.db.models.expressions import Random
from django.db.models.fields import CharField

# Create your models here.
class Brand(models.Model):
    brandname = models.CharField(max_length=50)
    product = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brandname} ({self.product})'

class Participants(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email

class Switches(models.Model):
    title = models.CharField(max_length=50)
    organizer_email = models.EmailField()
    spec = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Brand, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participants, blank=True, null=True)
    def __str__(self):
        return f'{self.title} - {self.slug}'

