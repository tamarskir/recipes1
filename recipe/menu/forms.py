from django import forms
from .models import Messages

class MessagesForm(forms.ModelForm):
   # date = forms.CharField(label="date", widget=forms.TextInput)
    name = forms.CharField(label=' your name', widget=forms.TextInput)
    messages = forms.CharField(label='add a review',widget=forms.Textarea)

    class Meta:
        model = Messages
        fields = ('name','messages')

    