from django.db import models

# Create your models here.
class SpeechText(models.Model):
    text = models.CharField(max_length=1000)
    language_code = models.CharField(max_length=3, default='en')
    file_name = models.CharField(max_length=250)

    def __str__(self):
        return self.text

class TranslatedStrings(models.Model):
    original_string = models.CharField(max_length=1000)
    translated_string = models.CharField(max_length=250)
    language_code = models.CharField(max_length=3, default='en')

class LanguageCodes(models.Model):
    language = models.CharField(max_length=250)
    language_code = models.CharField(max_length=3)