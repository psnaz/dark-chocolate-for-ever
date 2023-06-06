from django.conf import settings
from django.shortcuts import get_object_or_404

from .forms import NewsletterForm


def newsletter_form(request):
    form = NewsletterForm()
    context = {'newsletter_form': form}

    return context