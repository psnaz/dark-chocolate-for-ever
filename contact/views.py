from django.shortcuts import render
from django.http import HttpResponse


def contact_us(request):
    """ A view to show the contact page """
    return HttpResponse("Contact us with any questions you may have")
