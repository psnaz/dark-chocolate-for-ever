from django.urls import path
from . import views


urlpatterns = [
    path(
        'submit_review/<int:product_id>/',
        views.submit_review,
        name='submit_review'
    ),
]
