from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def quizzes(request):
    print(Quiz.objects.all())
    return render(request, 'base_blue.html')
