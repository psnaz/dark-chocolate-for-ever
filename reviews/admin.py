from django.contrib import admin
from .models import ProductReview


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'subject',
        'rating',
        'updated',
    )

    ordering = ('product',)
   
admin.site.register(ProductReview, ReviewsAdmin)
