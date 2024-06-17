from django import forms

from .models import Quiz, Question, Hint
from main_menu.views import current_user

class NewQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['quiz_name']
        
class QuizDetailForm(forms.ModelForm):
    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Quiz
        fields = ['questions']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = self.instance.questions.all()        
        
class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question_language'].initial = current_user.question_language
        self.fields['answer_language'].initial = current_user.answer_language

    class Meta:
        model = Question
        fields = ['question_text', 'question_language', 'answer_text', 'answer_language']
        
        
class HintForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hint_language'].initial = current_user.question_language
    class Meta:
        model = Hint
        fields = ['hint_text', 'hint_language', 'is_audio']