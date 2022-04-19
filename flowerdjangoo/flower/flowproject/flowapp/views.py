from django.shortcuts import render
from . models import Front

# Create your views here.
def home(request):
    obj = Front.objects.all()
    return render(request, 'home.html', {'result': obj})



