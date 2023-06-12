from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from .forms import NewsletterForm


def newsletter_signup(request):
    """ A view to handle post requests for newsletter sign-up form"""
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! You have been subscribed.')
            return redirect(url)
        else:
            messages.alert(request, "Sorry, something went wrong. Try again.")
            return redirect(url)
