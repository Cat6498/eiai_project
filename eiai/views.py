from django.shortcuts import render
from django.http import HttpResponse
from eiai.models import Deck, Card

# Create your views here.

def index(request):

    decks = Deck.objects.order_by('name')
    context_dict = {'boldmessage': 'lettura dei tarocchi per 2 franchi', 'decks': decks}
    return render(request, 'eiai/index.html', context_dict)
    

def show_deck(request, deck_name_slug):
    
    deck = Deck.objects.get(slug=deck_name_slug)
    cards = Card.objects.filter(deck=deck)
    
    context_dict = {'deck': deck, 'cards': cards }
    return render(request, 'eiai/show_deck.html', context_dict)

def about(request):
    
    context_dict = {'hello' : 'welcome to our website!'}
    return render(request, 'eiai/about.html', context_dict)


def daily_extraction(request, deck_name_slug):
    
    deck = Deck.objects.get(slug=deck_name_slug)
    cards = Card.objects.filter(deck=deck)
    if cards:    
        random_cards = cards.random(3)

    context_dict = {'deck': deck, 'random_cards': random_cards}
    return render(request, 'eiai/daily_extraction.html', context_dict)