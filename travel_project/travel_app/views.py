from django.shortcuts import render

from travel_app.models import Place


# Create your views here.
def index(request):
    obj = Place.objects.all()
    return render(request, "index.html", {'result':obj})


