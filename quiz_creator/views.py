from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import QuizForm

# Create your views here.


def quiz_list(request):
    if request.method == "GET":
        quizzes = Quiz.objects.all()
        form = QuizForm()
        return render(
            request,
            'quiz_creator/quiz_list.html',
            {'quizzes': quizzes, 'form': form}
        )
    # New quiz, POST request
    else:
        form = QuizForm(request.POST)
        if form.is_valid:
            new_quiz = form.save()


def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return (HttpResponse(quiz))
