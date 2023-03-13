from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_product_review, name='add_product_review'),
]
