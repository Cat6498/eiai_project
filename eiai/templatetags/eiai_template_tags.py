from django import template
from django.shortcuts import get_object_or_404
from eiai.models import Card, Word

register = template.Library()

@register.simple_tag
def get_words(card):
    try:
        words = card.words.filter(card=card)
    except Card.DoesNotExist:
        words = None
        
    return words


