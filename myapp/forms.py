from django import forms
from django.contrib.auth.models import User
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
                raise forms.ValidationError("Incorrect login or password.")


class SearchForm(forms.Form):
    title = forms.CharField(label='Article title', max_length=100)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "text", "publications"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=("Enter the same password as above for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)


class UserUpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)

    # error_messages = {
    #     'password_mismatch': ("The two password fields didn't match."),
    # }
    # password2 = forms.CharField(label=("Password confirmation"),
    #                             widget=forms.PasswordInput,
    #                             help_text=("Enter the same password as above for verification."))
    #
    #
    # def clean_password2(self):
    #     password = self.cleaned_data.get("password")
    #     password2 = self.cleaned_data.get("password2")
    #     if password and password2 and password != password2:
    #         raise forms.ValidationError(
    #             self.error_messages['password_mismatch'],
    #             code='password_mismatch',
    #         )
    #     return password2



