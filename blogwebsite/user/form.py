from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class Userregisterform(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=['username','email','password1','password2'] 

class Userupdateform(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
        
class Profileupdateform(forms.ModelForm):
    image=forms.ImageField()
    class Meta:
        model=Profile
        fields=['image']