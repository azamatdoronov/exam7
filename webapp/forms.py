from django import forms
from django.forms import widgets

from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        widgets = {
            "question": widgets.Textarea(attrs={"placeholder": "Введите свой вопрос"}),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["text_answer"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["poll", "choice"]
        widgets = {
            "choice": widgets.RadioSelect()
        }




