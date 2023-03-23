from django.shortcuts import render

from Travel_App.models import Place,People


# Create your views here.
def index(request):
    places=Place.objects.all()
    peoples=People.objects.all()

    return render(request,"index.html",{'place':places,'people':peoples})

