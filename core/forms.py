from logging import PlaceHolder
from django import forms
from core.models import Todo
from django.forms import DateInput

class DateInput(DateInput):
    input_type = 'date'
    PlaceHolder = 'Due Date'

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['title', 'due_date']
        widgets = {
            "title": forms.TextInput(attrs={"placeholder":"Enter your ToDO", 'size': '80', 'autocomplete': 'on'}),
            "due_date": DateInput
        }