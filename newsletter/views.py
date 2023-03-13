from django.shortcuts import render
from django.http import HttpResponse


def newsletter_signup(request):
    """ A view to show a newsletter sign-up page """
    return HttpResponse("Sign up for our newsletter")
