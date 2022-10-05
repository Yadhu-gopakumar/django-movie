
from django import forms
from movieApp.models import movie

class movieform(forms.ModelForm):
    class Meta:
        model = movie
        fields = ['img','year','name','desc']