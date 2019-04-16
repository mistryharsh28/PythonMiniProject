from django import forms

class TextSpeech(forms.Form):
    text = forms.CharField(label='text')
    language = forms.CharField(label='language')