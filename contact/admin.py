from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):

    list_display = (
        'full_name','subject', 'submitted',)

    ordering = ('-submitted',)

admin.site.register(ContactUs, ContactUsAdmin)
