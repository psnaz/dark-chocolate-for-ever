"""
This is my original custom model with associated functionalities that
hasn't been used in the CI Django Walkthrough projects.
"""

from django.db import models
from django.contrib.auth.models import User


class ContactUs(models.Model):
    """
    Model for contact form
    """
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.TextField(max_length=50)
    message = models.TextField()
    submitted = models.DateField(auto_now_add=True)
    answerdate = models.DateField(blank=True, null=True)
    username = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
