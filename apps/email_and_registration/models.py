from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime
from django.db import models
from ..wish_items.models import WishItem
# from django.contrib.auth.models import WishItem

class UserManager(models.Manager):
    def validate_register(self, registerData):
        errors = []
        letter_only_regex = '^[a-zA-Z]+$'
        email_format_regex = '^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'

        name_valid          = False
        username_valid      = False
        date_hired_valid    = False
        password_valid      = False
        password_conf_valid = False
        user_exists         = False

        # 3 chars
        if len(registerData['name']) > 3:
            name_valid = True
        if len(registerData['username']) > 3:
            username_valid = True

        if len(registerData['hired_at']) > 1:
            date_hired_valid = True

        # password exists, more than 8 chars
        if len(registerData['password']) > 8:
            password_valid = True
        # password matches password conf
        if registerData['password'] == registerData['password_conf']:
            password_conf_valid = True

        # check if email exists in the db
        user = User.objects.filter(username=registerData['username'])
        if len(user) > 0:
            user_exists = True

        if not name_valid:
            errors.append('Your name must be at least 3 characters.')
        if not username_valid:
            errors.append('Username must be atleast 3 characters.')
        if not date_hired_valid:
            errors.append('Need to fill in a date.')
        if not password_valid:
            errors.append('The password was not valid.')
        if not password_conf_valid:
            errors.append('The password confirmation did not match the password.')
        if user_exists:
            errors.append('The user already exists in the database. Try a different email.')

        return errors

    def validate_login(self, loginData):
        errors = []

        user = User.objects.filter(username=loginData['username']).first()

        if not user:
            errors.append('A user with that email doesnt exist in the database. Please register.')
        else:
            pwhash = user.password.encode()
            if pwhash == bcrypt.hashpw(loginData['password'].encode(), pwhash):
                print 'PASSWORD MATCHED!!!'
            else:
                errors.append('User with that email exists, but password was incorrect.')

        if user:
            return (user.id, errors)
        else:
            return (None, errors)

    def encrypt_password(self, userObj):
        if not 'password' in userObj:
            return False
        hashed = bcrypt.hashpw(userObj['password'].encode(), bcrypt.gensalt())
        user_obj = {
            'name':       userObj['name'],
            'username':   userObj['username'],
            'hired_at': userObj['hired_at'],
            'password':   hashed
        }
        return user_obj

    # def get_user()


# Create your models here.
class User(models.Model):
    name       = models.CharField(max_length=255)
    username   = models.CharField(max_length=255)
    password   = models.CharField(max_length=255)
    hired_at   = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wish_items = models.ManyToManyField(WishItem)
    objects    = UserManager()

    # def __unicode__(self):
    #     return "%s (%s)" % (self.email, self.group[:10])
