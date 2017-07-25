# coding: utf-8
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=255)
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=255)