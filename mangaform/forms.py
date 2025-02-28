from django import forms

class MangaForm(forms.Form):
    character = forms.CharField(max_length=100, label='Manga Character')
    manga = forms.CharField(max_length=100, label='Manga')