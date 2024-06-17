from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.quiz_list, name='quizzes'),
    path('quizzes/quiz/<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('quizzes/question/<int:pk>/', views.question_detail, name='question_detail'),
    path('quizzes/hints/<int:pk>/', views.hints, name='hints'),
    path('quizzes/hint/<int:pk>/', views.hint_detail, name='hint_detail'),
]
