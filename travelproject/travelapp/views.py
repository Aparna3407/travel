from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Place,Team


def index(request):
    obj=Place.objects.all()
    objt=Team.objects.all()
    return render(request,'index.html',{'display':obj,'result':objt})