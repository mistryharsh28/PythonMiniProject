from gtts import gTTS
from playsound import playsound
from . models import SpeechText, TranslatedStrings
from django.utils import timezone
import requests
from urllib.parse import quote
from textblob import TextBlob
from textblob.exceptions import NotTranslated

def get_speech_from_text(text, language_code):
    try:
        speech_file = SpeechText.objects.get(text=text, language_code=language_code)
        file_name = speech_file.file_name
    except SpeechText.DoesNotExist:
        try:
            translated_text = get_translated_string(text, language_code)
            speech_object = gTTS(translated_text, lang=language_code, slow=False)
        except ValueError:
            translated_text = get_translated_string(text, language_code)
            speech_object = gTTS(translated_text, lang='en', slow=False)
        file_name = str(int(SpeechText.objects.all().last().file_name) + 1)
        speech_object.save('app/static/speech_files/{}.mp3'.format(file_name))
        speech_file = SpeechText(text=text, file_name=file_name, language_code=language_code)
        speech_file.save()

    playsound('app/static/speech_files/{}.mp3'.format(file_name))
    return file_name
    # play the sound here or just send the mp3 file

def get_translated_string(original_string, language_code):
    try:
        translated_string_object = TranslatedStrings.objects.get(original_string = original_string, language_code=language_code)
        return translated_string_object.translated_string
    except TranslatedStrings.DoesNotExist:
        try:
            try:
                translated_string = TextBlob(original_string.lower()).translate(to=language_code)
                translated_string = str(translated_string)

            except NotTranslated:
                try:
                    url = 'https://inputtools.google.com/request?text={0}&ime=transliteration_en_{1}&num=1&ie=utf-8&oe=utf-8'.format(quote(original_string), language_code)

                    response = requests.get(url)
                    if response.status_code != 200:
                        return original_string

                    api_response_data = response.json()
                    translated_string = api_response_data[1][0][1][0]
                except Exception:
                    return original_string

            TranslatedStrings(
                original_string = original_string,
                translated_string = translated_string,
                language_code=language_code
            ).save()

            return translated_string
        # this depends on a lot of things to not change

        except Exception:
            return original_string

        return original_string

def get_literal_translation_string(original_string, language_code):
    if language_code == "en":
        return original_string

    try:
        translated_string_object = LiteralTranslatedStrings.objects.get(original_string = original_string, language_code=language_code)
        return translated_string_object.translated_string
    except LiteralTranslatedStrings.DoesNotExist:
        try:
            url = 'https://inputtools.google.com/request?text={0}&ime=transliteration_en_{1}&num=1&ie=utf-8&oe=utf-8'.format(quote(original_string), language_code)

            response = requests.get(url)
            if response.status_code != 200:
                return original_string

            api_response_data = response.json()
            translated_string = api_response_data[1][0][1][0]

            LiteralTranslatedStrings(
                original_string = original_string,
                translated_string = translated_string,
                language_code=language_code
            ).save()

            return translated_string

        except Exception:
            return original_string

        return original_string