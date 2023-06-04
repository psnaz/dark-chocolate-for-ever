from django import forms
# from .widgets import CustomClearbleFileInput
from .models import Product, ProductReview


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ['subject', 'review', 'rating']
