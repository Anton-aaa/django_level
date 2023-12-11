from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.forms import TextInput

from myapp.models import Article, Comment


class RegisterForm(forms.Form):
    username = forms.CharField(label='New username', max_length=100)
    password = forms.CharField(label='New password', max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        nickname = cleaned_data.get('username')
        if str(password) in nickname:
            self.add_error('password', "Password can't be in nickname")

class MyForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length=100)
    age = forms.IntegerField(label='My age')

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        nickname = cleaned_data.get('nickname')
        if str(age) in nickname:
            self.add_error('age', "Age can't be in nickname")

class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError("No profile")


class SearchForm(forms.Form):
    title = forms.CharField(label='Article title', max_length=100)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "text"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]



