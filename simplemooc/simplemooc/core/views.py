from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
#    return HttpResponse("Hello world")

def home(request):
    return render(request, 'home.html', {'usuario':'Fulano de Tal'})

