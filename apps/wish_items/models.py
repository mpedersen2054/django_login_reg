from __future__ import unicode_literals
# from ..email_and_registration.models import User
from django.db import models
# User = models.get_model('email_and_registration', 'User')
# from django.apps import apps
# User = apps.get_model('email_and_registration', 'User')
# from ..email_and_registration.models import User

# Create your models here.
class WishItem(models.Model):
    name       = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id       = models.ForeignKey('email_and_registration.User', on_delete=models.CASCADE)
