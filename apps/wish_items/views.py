from django.shortcuts import render, redirect
from .models import WishItem
from ..email_and_registration.models import User

# Create your views here.
def show_item(request, id):
    wish_item = WishItem.objects.filter(id=id).first()
    context = {
        'id': id,
        'item': wish_item
    }
    return render(request, 'wish_items/show_item.html', context)

def new(request):
    return render(request, 'wish_items/new.html')

def create(request):
    print request.POST
    user = User.objects.filter(id=request.session['user_id']).first()
    print 'USER', user
    # need validation eventually
    wish_item = WishItem(name=request.POST['item_name'], user_id=user)
    wish_item.save()
    user.wish_items.add(wish_item)
    user.save()
    return redirect('users:dashboard')

def remove_item(request, id):
    print request.POST
    print 'ID: ', id
    return redirect('users:dashboard')
