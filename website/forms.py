from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(Label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(Label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(Label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

