from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('terms', views.terms, name='terms'),
    path('hampers', views.hampers, name='hampers'),
    path('vouchers', views.vouchers, name='vouchers'),
    path('subscriptions', views.subscriptions, name='subscriptions'),
]
