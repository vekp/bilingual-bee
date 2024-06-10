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
        return f"Q: {self.question_text} A: {self.answer_text}"

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.quiz_name

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()  # New order field

    class Meta:
        unique_together = ('quiz', 'question')
        ordering = ['order']  # Default ordering by order field

    def __str__(self):
        return f"{self.quiz} - {self.question} (Order: {self.order})"

class Hint(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint_text = models.TextField()
    is_audio = models.BooleanField(default=False)
    hint_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Hint for {self.question}: {self.hint_text}"
