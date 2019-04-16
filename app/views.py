from django.shortcuts import render
from .forms import TextSpeech
from .translator import get_speech_from_text
from playsound import playsound
from time import sleep
# Create your views here.

def Home(request):
    playsound('app/static/speech_files/greetings.wav')
    return render(request, 'app/index-2.html', {})

def TextToSpeech(request):
    if request.method == "POST":
        form = TextSpeech(request.POST)
        text = form.data['text']
        language = form.data['language']
        if language.lower() == 'marathi':
            language_code = 'mr'
        else:
            language_code = language[:2].lower()
        get_speech_from_text(text, language_code)
    return render(request, 'app/index-2.html', {})