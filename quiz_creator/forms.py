from django import forms

from .models import Quiz, Question

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
        
