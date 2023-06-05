from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='contacts'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('contact-submitted', views.contact_submitted, name='contact_submitted')
]
