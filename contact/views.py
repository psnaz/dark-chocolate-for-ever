"""
This is my original custom model with associated functionalities that
hasn't been used in the CI Django Walkthrough projects. It has been
created by following and tweaking the Youtube Django Tutorial #9:
A More Complex Form (2022) by Django tutorials (see README file)
AND with a kind advice and help of my mentor.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from .models import ContactUs
from .forms import ContactForm


def contact(request):
    """ A view to display contact page"""
    return render(request, 'contact/contact.html')
