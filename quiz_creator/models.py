from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    answer_text = models.CharField(max_length=50)
    question_language = models.ForeignKey(Language, related_name='question_language', on_delete=models.CASCADE)
    answer_language = models.ForeignKey(Language, related_name='answer_language', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question_text} | {self.answer_text}"

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=50, unique=True)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.quiz_name


class Hint(models.Model):
    question = models.ForeignKey(Question, related_name='hints', on_delete=models.CASCADE)
    hint_text = models.CharField(max_length=100)
    hint_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    is_audio = models.BooleanField(default=False)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Hint for {self.question}: {self.hint_text}"
