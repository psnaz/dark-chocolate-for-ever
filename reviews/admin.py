from django.contrib import admin
from .models import ProductReview


class ReviewsAdmin(admin.ModelAdmin):
    readonly_fields = ('submitted', 'subject', 'review', 'rating', 'ip', 'user', 'status', 'updated',)

    fields = ('full_name', 'email', 'submitted', 'subject', 'review', 'rating', 'ip', 'user', 'updated',)

    list_display = ('full_name', 'email', 'submitted', 'subject', 'review', 'rating', 'updated',)

    ordering = ('-submitted',)
    
admin.site.register(ProductReview, ReviewsAdmin)
