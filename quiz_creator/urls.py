from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.quiz_list, name='quizzes'),
    path('quizzes/<int:pk>/', views.quiz_detail, name='quiz_detail'),
]
