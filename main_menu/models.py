from django.db import models

from quiz_creator.models import *

class User(models.Model):
    question_language = models.ForeignKey(Language, related_name='user_question_language', on_delete=models.CASCADE)
    answer_language = models.ForeignKey(Language, related_name='user_answer_language', on_delete=models.CASCADE)

