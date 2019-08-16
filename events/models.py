from django.db import models
from django.forms import ModelForm, Form, CharField, TextInput, EmailField, PasswordInput, DateInput
from django.contrib.auth.models import User
from django import forms
from projectABC import settings
from datetime import date

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class Event(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    place = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=1000, null=True)
    initialDate = models.DateField(default=date.today)
    finalDate = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Event: ' + self.name

class EventForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    place = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    initialDate = forms.DateField(initial=date.today, widget=forms.DateInput(
        attrs={'class': 'form-control', 'type':'date'}
    ))
    finalDate = forms.DateField(initial=date.today, widget=forms.DateInput(
        attrs={'class': 'form-control', 'type':'date'}
    ))

    class Meta:
        model = Event
        fields = ['name', 'category', 'place', 'address', 'initialDate', 'finalDate']

    def save(self, user):
        obj = super().save(commit=False)
        obj.user = user
        obj.save()
        return obj


class SignInForm(Form):
    username = CharField(max_length=50, widget=TextInput(
        attrs={'class': 'form-control'}
    ), required=True)
    password = CharField(min_length=8, max_length=10, widget=PasswordInput(
        attrs={'class': 'form-control'}
    ), required=True)