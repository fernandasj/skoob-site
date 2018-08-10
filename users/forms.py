from django import forms
from .models import Profile

class RegisterUser(forms.ModelForm):

    email = forms.EmailField()

    username = forms.CharField()

    password = forms.CharField()

    class Meta:
        model = Profile
        fields = ('name', 'gender')
