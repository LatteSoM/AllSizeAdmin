from django import forms
from api_app.models import Users
from rest_framework.authtoken.models import Token


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('login', 'password')


class UserLoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
