from django.urls import path
from . import views


urlpatterns = [
    path('newsletter', views.newsletter_signup, name='newsletter_signup'),
]
