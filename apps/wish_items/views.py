from django.shortcuts import render

# Create your views here.
def show_item(request, id):
    context = {
        'id': id
    }
    return render(request, 'wish_items/show_item.html', context)

def new(request):
    return render(request, 'wish_items/new.html')
