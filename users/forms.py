from django import forms
from django.contrib.auth.forms import UserChangeForm, BaseUserCreationForm,  AuthenticationForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-auth_au',
    }))
    
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(BaseUserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-auth_au',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-auth_au',
    }))
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        

class UserProfileForm(UserChangeForm):
    CHOICES = [
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    ]
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-auth_au',
    }), required= False)
    profession = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required= True)
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'class': 'forms-auth_au'}), choices=CHOICES, required=True)
    age = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    town = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'profession', 'gender', 'age', 'town')
        
        
class CreateResume(forms.ModelForm):
    CHOICES = [
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    ]
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-auth_au',
    }), required= False)
    profession = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'class': 'forms-auth_au'}), choices=CHOICES, required=True)
    age = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    town = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-auth_au',
    }), required=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'profession', 'gender', 'age', 'town')