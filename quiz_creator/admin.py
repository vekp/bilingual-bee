from django.contrib import admin
from .models import Question, Quiz, QuizQuestion, Hint, Language

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(Hint)
admin.site.register(Language)