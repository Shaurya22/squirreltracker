from django.forms import ModelForm
from .models import Squirrels
from django.db import models
from django import forms
class SquirrelForm(ModelForm):
    
    Specific_location = forms.CharField(required=False)
    Other_Activities = forms.CharField(required=False)
    class Meta:
        model = Squirrels
        fields = '__all__'
