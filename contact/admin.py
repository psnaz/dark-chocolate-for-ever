from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = ('submitted',)

    fields = ('full_name', 'email', 'username', 'submitted', 'subject', 'message',)

    ordering = ('-submitted',)

admin.site.register(ContactUs, ContactUsAdmin)
