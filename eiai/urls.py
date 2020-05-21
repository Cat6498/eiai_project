from django.urls import path
from eiai import views

app_name = 'eiai'

urlpatterns = [
    path('', views.index, name='index'),
    path('deck/<slug:deck_name_slug>/', views.show_deck, name='show_deck'),
    path('deck/<slug:deck_name_slug>/daily_extraction', views.daily_extraction, name='daily_extraction'),
    path('about', views.about, name="about"),
    path('register/', views.register, name='register'),
]
