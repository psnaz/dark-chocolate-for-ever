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
from .models import ContactUs
from .forms import ContactUsForm


def index(request):
    """
    Renders the success page after submitting the contact form
    """
    template = 'contact/contact-us.html'

    contact_form = ContactUsForm()

    context = {
        'contact_form': contact_form
    }

    return render(request, template, context)


def contact_us(request):
    """ 
    A view to show the contact page 
    """
    form = ContactUsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('contact_submitted')
    
    return HttpResponse('Something went wrong')


def contact_submitted(request):
    return render(request, 'contacts/index.html')
