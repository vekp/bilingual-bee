from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# TODO: create real users, implement session
current_user = get_object_or_404(User, pk=1)

# Create your views here.
def index(request):
    return render(request, 'main_menu/main_menu.html')
