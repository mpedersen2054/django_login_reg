from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User

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
    else:
        user_with_encrypted = User.objects.encrypt_password(request.POST)
        User.objects.create(
            first_name = user_with_encrypted['first_name'],
            last_name = user_with_encrypted['last_name'],
            email = user_with_encrypted['email'],
            password = user_with_encrypted['password']
        )
        messages.success(request, 'Successfully registered user.')
    return redirect(reverse('users:index'))

def login(request):
    # returns tuple (id, [errors...])
    login = User.objects.validate_login(request.POST)
    user_id = login[0]
    errors = login[1]
    print errors
    if len(errors) > 0 or not user_id:
        for error in errors:
            messages.error(request, error)
    else:
        request.session['user_id'] = user_id
        messages.success(request, 'Successfully logged in.')
    return redirect(reverse('users:index'))

# def success(request):
#     if not 'user_id' in request.session:
#         return redirect('/')
#     context = {
#         'user': User.objects.filter(id=request.session['user_id']).first()
#     }
#     messages.success(request, 'Successfully logged in!')
#     return render(request, 'email_and_registration/success.html', context)
