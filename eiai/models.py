from django.db import models
from django.template.defaultfilters import slugify
from django_random_queryset import RandomManager
from django.contrib.auth.models import User


# Create your models here.

class Deck(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(help_text = "Enter a description", blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Deck, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name



class Word(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Card(models.Model):

    objects = RandomManager()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='taarot_images', blank=True)
    number = models.IntegerField()
    words = models.ManyToManyField(Word, blank=True)
    description = models.TextField(help_text = "Enter a description", blank=True)

    def __str__(self):
        return self.name



class Address(models.Model):

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    country = models.CharField(
        "Country",
        max_length=30,
    )


    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return self.address1



class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    addresses = models.ManyToManyField(Address, blank=True)

    def __str__(self):
        return self.user.username
    


class DailyExtraction(models.Model):

    usedDeck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    pickedCards = models.ManyToManyField(Card, blank = True)
    date = models.DateField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)