from django import forms
from .models import TweetModal

class TweetModalForm(forms.ModelForm):
    class Meta:
        model = TweetModal
        fields = ['content']