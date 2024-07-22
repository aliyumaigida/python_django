from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="optional")
    email = forms.CharField(max_length=254, help_text="Enter a valid email address")


    class Meta:
        model = User
        fields = [
           'username',
           'first_name',
           'last_name',
           'email',
           'password1',
           'password2',
        ]

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        # can call "staff_form" any name

class Profile_form(forms.ModelForm):    
    gend = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    Profile_passport = forms.ImageField(required=False, label='Profile passport')
    means_of_identity = forms.ImageField(required=False, label='Means of identity')
    particulars = forms.FileField(required=False, label='particulars')
    gender = forms.ChoiceField(choices=gend, required=True, widget=forms.RadioSelect)
    class Meta:  
        model = Profile
        fields = [
           'address',
           'phone',
           'date_of_birth',
           'gender',
           'nationality',
           'state',
           'means_of_identity',
           'particulars',
           'profile_passport',
           'position',
           'marital_status',
           'staff',
           'next_of_kin',
        ]   
        widgets= {
            'date_of_birth': forms.NumberInput(attrs={'type': 'date'}),
        }   
        