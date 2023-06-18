from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'email',
        'date',
    )

    ordering = ('-date',)


admin.site.register(Newsletter, NewsletterAdmin)
