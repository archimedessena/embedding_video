from django.shortcuts import render
from .models import Item


# Create your views here.
#video
def video(request):
    obj = Item.objects.all()
    return render(request, "v.html", {'obj': obj})