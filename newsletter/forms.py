from django.forms import ModelForm
from . models import Newsletter


class NewsletterForm(ModelForm):
    """
    Form for newsletter signup
    """
    class Meta:
        model = Newsletter
        fields = '__all__'
