from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        VEGETARIAN = 'VG', 'Vegetarian'
        NONVEGETARIAN = 'NV', 'Non Vegetarian'
        OTHER = 'OT', 'Other'

    name = models.TextField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField(validators=[MaxValueValidator(-90), MinValueValidator(90)])
    longitude = models.FloatField(validators=[MaxValueValidator(-180), MinValueValidator(180)])
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self) -> str:
        return self.name
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self) -> str:
        return f'Rating: {self.rating}'
    
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()