from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def quiz_list(request):
    # Display list of all quizzes
    if request.method == "GET":
        quizzes = Quiz.objects.all()
        form = NewQuizForm()
        return render(
            request,
            'quiz_creator/quiz_list.html',
            {'quizzes': quizzes, 'form': form}
        )
    # New quiz, POST request
    else:
        form = NewQuizForm(request.POST)
        # Create new quiz, redirect to its edit page
        if form.is_valid:
            new_quiz = form.save()
            return redirect('quiz_detail', new_quiz.pk)
        else:
            return HttpResponse("Invalid input")
            


def quiz_detail(request, pk):
    all_questions = Question.objects.all()
    quiz = get_object_or_404(Quiz, pk=pk)
    form = QuizDetailForm()
    if request.method == "GET":
        return (render(
            request,
            'quiz_creator/quiz_detail.html',
            {'quiz': quiz, 'form': form, 'all_questions': all_questions}
        ))
    else:
        selected_questions = request.POST.getlist("question")
        for question in all_questions:
            if str(question.pk) in selected_questions:
                quiz.questions.add(question)
            else:
                quiz.questions.remove(question)
        return HttpResponse("Nice")
        