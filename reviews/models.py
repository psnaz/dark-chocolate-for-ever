"""
This is my original custom model with associated functionalities that 
hasn't been used in the CI Django Walkthrough projects. It has been 
created by following the Youtube Django Tutorial #9: A More Complex Form (2022) 
by Django tutorials (see README file)
"""

from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class ProductReview(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    submitted = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
