from django.db import models


# Create your models here.

class Clothes(models.Model):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    EXTRA_LARGE = "XL"
    SIZE_CHOICES = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, "Large"),
        (EXTRA_LARGE, 'Extra Large'),
    )
    SUMMER = "SUMMER"
    AUTUMN = "AUTUMN"
    WINTER = "WINTER"
    SPRING = "SPRING"
    SEASON_CHOICES = (
        (SUMMER, 'Summer'),
        (AUTUMN, 'Autumn'),
        (WINTER, 'Winter'),
        (SPRING, 'Spring')
    )
    title = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    price = models.IntegerField(default=100, null=True, blank=True)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default=MEDIUM)
    discount = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    season = models.CharField(max_length=6, choices=SEASON_CHOICES, default=SUMMER)
    supplier = models.ForeignKey('Suppliers', null=True, on_delete=models.SET_NULL)


class Category(models.Model):
    clothes_type = models.CharField(max_length=20)


class Suppliers(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

