from django.shortcuts import render
from django.http import HttpResponse


def add_product_review(request):
    # A view to allow user to create a product review 
    return HttpResponse("Add your product review")

