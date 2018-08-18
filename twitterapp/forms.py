from django import forms
from .models import Tweet
from django.contrib.auth.models import User

class AddTweetForm(forms.Form):
    content =forms.CharField(max_length=200)


    '''
    class Meta:
        model = Tweet
        fields='__all__'
        exclude = '__user__'
    '''