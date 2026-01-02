from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.contrib.auth import authenticate


class Registration(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        

class Login(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        
        user=authenticate(username=email,password=password)
        if not user:
            raise forms.ValidationError("Invalid User")
        self.user=user
        return self.cleaned_data
    def get_user(self):
        return self.user
    