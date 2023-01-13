from django.shortcuts import render
from django.http import HttpResponse
from .models import Rating

# Create your views here.
def review(request):
    x=Rating.objects.all()
    return render(request,'index.html',{'x':x})
    #return HttpResponse("<h1> welcome to meesho</h1>")
