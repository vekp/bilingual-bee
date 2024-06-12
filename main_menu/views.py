from django.shortcuts import render
from django.http import HttpResponse #TODO remove

# Create your views here.
def index(request):
    return render(request, 'main_menu/main_menu.html')
