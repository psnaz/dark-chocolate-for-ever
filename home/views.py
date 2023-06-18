from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def terms(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/terms.html')


def hampers(request):
    """ A view to return the hampers page """

    return render(request, 'home/hampers.html')


def vouchers(request):
    """ A view to return the vouchers page """

    return render(request, 'home/vouchers.html')


def subscriptions(request):
    """ A view to return the subscriptions page """

    return render(request, 'home/subscriptions.html')
