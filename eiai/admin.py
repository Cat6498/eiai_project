from django.contrib import admin
from eiai.models import Deck, Word, Card

class DeckAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


# Register your models here.
admin.site.register(Deck, DeckAdmin)
admin.site.register(Word)
admin.site.register(Card)
