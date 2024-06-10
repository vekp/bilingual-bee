from django.shortcuts import render
from django.http import HttpResponse #TODO remove

# Create your views here.
def index(request):
    return render(request, 'base.html')
    return HttpResponse('Hello!! Welcome.')#TODO remove