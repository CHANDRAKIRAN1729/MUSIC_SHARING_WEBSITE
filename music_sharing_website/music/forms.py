from django import forms
from .models import MusicFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MusicFileForm(forms.ModelForm):
    class Meta:
        model = MusicFile
        fields = ('file', 'visibility', 'allowed_emails')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']