from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import User
from ..wish_items.models import WishItem

# Create your views here.
def index(request):
    if not 'user_id' in request.session:
        request.session['user_id'] = None
    context = {
        'users': User.objects.all()
    }
    return render(request, 'email_and_registration/index.html', context)

def register(request):
    errors = User.objects.validate_register(request.POST)

    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('users:index')
    else:
        user_with_encrypted = User.objects.encrypt_password(request.POST)
        new_user = User.objects.create(
            name       = user_with_encrypted['name'],
            username   = user_with_encrypted['username'],
            hired_at = user_with_encrypted['hired_at'],
            password   = user_with_encrypted['password']
        )
        request.session['user_id'] = new_user.id
        messages.success(request, 'fully registered user.')
        return redirect('users:dashboard')

def login(request):
    login = User.objects.validate_login(request.POST)
    user_id, errors = login
    if len(errors) > 0 or not user_id:
        for error in errors:
            messages.error(request, error)
        return redirect('users:index')
    else:
        request.session['user_id'] = user_id
        messages.success(request, 'fully logged in!')
        return redirect('users:dashboard')

def dashboard(request):
    if not 'user_id' in request.session \
    or request.session['user_id'] == None:
        messages.error(request, 'You need to be logged in to go to that route.')
        return redirect('users:index')


    # get all users wishlist, get a few other ppls wishlist items
    user = User.objects.filter(id=request.session['user_id']).first()

    # get 5 wish items that arent the users
    wish_items = WishItem.objects.filter(user=None)
    all_wish_items = WishItem.objects.all()
    context = {
        'user': user,
        'not_user_wish_items': wish_items,
        'all_wish_items': all_wish_items
    }
    # messages.success(request, 'fully logged in!')
    return render(request, 'email_and_registration/dashboard.html', context)

def logout(request):
    request.session.flush()
    messages.success(request, 'fully logged out!')
    return redirect('users:index')
