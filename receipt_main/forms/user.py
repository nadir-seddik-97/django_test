from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from ..models import Users

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','address','phone','photo')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    def clean(self):
        cleaned_data = super().clean()
       # logged in user
        user = self.user_cache  
        
        
        if user.is_authenticated:
         return cleaned_data
