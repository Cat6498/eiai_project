from django.db import models
from django.template.defaultfilters import slugify
from django_random_queryset import RandomManager

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
