from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('text_to_speech/', views.TextToSpeech, name='text_to_speech'),
]
