from django import forms
from .models import Strawhats

class ApplicationForm(forms.Form):
    name = forms.CharField(
        label='Name of User', 
        min_length=5, 
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Jane Smith'})
    )
    address = forms.CharField(
        label='Address',
        max_length=100,
    )
    posts = (
        ('Manager', 'Manager'),
        ('Cashier', 'Cashier'),
        ('Operator', 'Operator'),
    )
    field = forms.ChoiceField(
        choices=posts
    )
    age = forms.IntegerField(
        label='Age',
        min_value=18,
        max_value=66,
        required=False
    )
    email = forms.EmailField(
        label='you email address',
        widget=forms.EmailInput(attrs={'placeholder': 'jane.smith@email.com'})
    )
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    gender = forms.ChoiceField(
        choices=GENDER
    )
    
# Model Form for Strawhat model
class StrawhatForm(forms.ModelForm):
    class Meta:
        model = Strawhats
        fields = ('name', 'position', 'member', 'gender')
            
    
    