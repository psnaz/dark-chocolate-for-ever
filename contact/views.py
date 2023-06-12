"""
This is my original custom model with associated functionalities that
hasn't been used in the CI Django Walkthrough projects. It has been
created by following and tweaking the Youtube Django Tutorial #9:
A More Complex Form (2022) by Django tutorials (see README file)
AND with a kind advice and help of my mentor.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from .models import ContactUs
from .forms import ContactForm


def contact(request):
    """
    A view to handle post requests for contact form
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Success! Your email's been submitted.")
            return redirect('home')
        else:
            messages.error(request, "Sorry, something went wrong. Try again.")
    else:
        contact_form = ContactForm()
    context = {'contact_form': contact_form}
    return render(request, 'contact/contact.html', context)
