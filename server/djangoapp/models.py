from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_founded = models.PositiveIntegerField(
        default=2026, 
        validators=[MinValueValidator(1900), MaxValueValidator(2099)])

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('MUSCLE', 'Muscle'),
        ('SUPERCAR', 'Supercar'),
        ('LOWRIDER', 'Lowrider'),
    ]
    type = models.CharField(
        max_length=10, 
        choices=CAR_TYPES, 
        default='SEDAN')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    num_doors = models.IntegerField(
        default=4,
        validators=[
            MaxValueValidator(2),
            MinValueValidator(6)
        ])


    def __str__(self):
        return self.name
