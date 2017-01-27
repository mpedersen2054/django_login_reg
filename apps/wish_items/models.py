from __future__ import unicode_literals
from django.db import models

class WishItem(models.Model):
    name       = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id    = models.ForeignKey('email_and_registration.User', on_delete=models.CASCADE)
