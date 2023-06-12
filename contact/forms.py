"""
This is my original custom model with associated functionalities that
hasn't been used in the CI Django Walkthrough projects. It has been
created by following and tweaking the Youtube Django Tutorial #9:
A More Complex Form (2022) by Django tutorials (see README file)
AND with a kind advice and help of my mentor.
"""

from django import forms
from django.forms import ModelForm
from .models import ContactUs


class ContactForm(ModelForm):
    """
    Form for contact us page
    """
    class Meta:
        model = ContactUs
        fields = '__all__'
