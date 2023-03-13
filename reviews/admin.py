from django.contrib import admin
from .models import ProductReview


class ReviewsAdmin(admin.ModelAdmin):
    readonly_fields = ('submitted', 'message',)

    fields = ('full_name', 'email', 'submitted', 'message',)

    list_display = ('full_name', 'email', 'submitted', 'message')

    ordering = ('-submitted',)   

admin.site.register(ProductReview, ReviewsAdmin)
