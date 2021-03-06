# Generated by Django 3.0.6 on 2020-05-18 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, help_text='Enter a description')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='taarot_images')),
                ('number', models.IntegerField()),
                ('description', models.TextField(blank=True, help_text='Enter a description')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eiai.Deck')),
                ('words', models.ManyToManyField(blank=True, to='eiai.Word')),
            ],
        ),
    ]
