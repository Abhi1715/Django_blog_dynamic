from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blogs.models import Blog
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author', 'created_at', 'updated_at','slug','is_featured']