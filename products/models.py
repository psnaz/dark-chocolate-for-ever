from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=100)
    format = models.CharField(max_length=120)
    flavour = models.CharField(max_length=120)
    units = models.CharField(max_length=120)
    cocoa_mass = models.CharField(max_length=100, null=True, blank=True)
    diet_type = models.CharField(max_length=120, null=True, blank=True)
    speciality = models.CharField(max_length=254, null=True, blank=True)
    size = models.CharField(max_length=120)
    ingredients = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name
