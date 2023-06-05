from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, ProductReview
from .forms import ReviewForm


@login_required
def submit_review(request, product_id):
    """ A view to allow user to submit a product review """
  
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        try:
            reviews = ProductReview.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        
        except ProductReview.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ProductReview()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)
    