from django.db import models

# Create your models here.

class Amenities(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Hotels(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.TextField()
    hotel_price = models.IntegerField()
    hotel_image = models.CharField(max_length=500)
    amenities = models.ManyToManyField(Amenities)
    
    
    def __str__(self):
        return self.hotel_name  