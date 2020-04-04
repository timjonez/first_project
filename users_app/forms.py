from django import forms
from django.contrib.auth.models import User
from .models import UserProfile_Model


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfile_Form(forms.ModelForm):
    class Meta():
        model = UserProfile_Model
        fields = ('portfilio_site', 'profile_pic')
