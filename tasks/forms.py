from django import forms

class TaskFormular(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'New task',
            'required': True
        })
    )