from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from eiai.models import Deck, Card, UserProfile, Address, DailyExtraction
from eiai.forms import AddressForm, UserForm
import datetime

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


@login_required
def daily_extraction(request, deck_name_slug):

    try:
        extraction = DailyExtraction.objects.get(user=request.user, date=datetime.date.today())
    except DailyExtraction.DoesNotExist:
        extraction = None
    
    if extraction:
        check = True
    
    else:
        deck = Deck.objects.get(slug=deck_name_slug)
        cards = Card.objects.filter(deck=deck)
        if cards:    
            random_cards = cards.random(3)

        extraction = DailyExtraction()
        extraction.user = request.user
        extraction.usedDeck = deck
        extraction.save()
        extraction.pickedCards.set(random_cards)
        check = False

    context_dict = {'extraction': extraction, 'check': check}
    return render(request, 'eiai/daily_extraction.html', context_dict)


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        address_form = AddressForm(request.POST)
        
        if user_form.is_valid() and address_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            address = address_form.save()
            address.save()
            profile = UserProfile(user=user)
            profile.save()
            profile.addresses.add(address)
            registered = True

        else:
            print(user_form.errors, address_form.errors)
    
    else:
        user_form = UserForm()
        address_form = AddressForm()

    return render(request, 'eiai/register.html', context = {'user_form': user_form, 
                            'address_form': address_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('eiai:index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print(f"invakid login details: {username}, {password}")
            return HttpResponse("Invalid login details")

    else:
            return render(request, 'eiai/login.html')

    
@login_required
def user_logout(request):

    logout(request)
    return redirect(reverse('eiai:index'))