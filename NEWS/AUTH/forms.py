from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserRegister(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_passwordConfirm(self):
        data = self.cleaned_data
        if data['password'] != data['password_confirm']:
            raise forms.ValidationError("Passwords are not similar !!!")
        return data['password_confrim']

class UserEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']