from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Max
from .models import *
from .forms import *
from main_menu.views import current_user


def quiz_list(request):
    """
    Render a list of all existing quizzes in response to GET request,
    or create a new quiz in response to POST request.
    """
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
    """
    GET: Display all existing questions, with  checkboxes to select questions for the quiz.
    POST: Save all checked questions to current quiz.
    """
    global current_quiz
    current_quiz = pk
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
        return redirect('quizzes')
        #TODO: Add success message/popup
    
def question_detail(request, pk):
    """
    GET: Display form with details for a question.
    POST: Save details after validating.
    """
    global current_question
    current_question = pk
    if Question.objects.filter(pk=pk).exists():
        question = get_object_or_404(Question, pk=pk)
    else:
        question = None

    if request.method == "GET":
        form = QuestionForm(instance=question)
        return render(request,
                    'quiz_creator/question_detail.html',
                    {'question': form.instance, 'form': form}
                    )
    else:
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('quiz_detail', current_quiz)
            #TODO: Add success message/popup


def hints(request, pk):
    """
    Display list of all hints for current question.
    """
    global current_question
    current_question = pk
    if request.method == "GET":
        question = get_object_or_404(Question, pk=pk)
        hints = question.hints.all()
        form = HintForm()
        return render(request, 'quiz_creator/hints.html', {'hints': hints, 'question': question, 'form': form})
    #TODO: Make hints sortable
    
def hint_detail(request, pk):
    """
    GET: Display form for editing existing hint, or creating new one.
    POST: Save hint details.
    """
    if Hint.objects.filter(pk=pk).exists():
        hint = get_object_or_404(Hint, pk=pk)
    else:
        hint = None
        
    if request.method == "GET":
        form = HintForm(instance=hint)
        return render(request, 'quiz_creator/hint_detail.html', {'hint': form.instance, 'form': form})
    else:
        form = HintForm(request.POST, instance=hint)
        hint = form.save(commit=False)
        # Add question and order to make valid obj
        hint.question = get_object_or_404(Question, pk=current_question)
        if hint.order is None:
            max_order = Hint.objects.filter(question=current_question).aggregate(Max('order'))['order__max']
            hint.order = max_order + 1 if max_order else 1
        
        if form.is_valid():
            form.save()
            return redirect('hints', current_question)
            #TODO: Add success message/popup
