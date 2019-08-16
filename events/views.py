from django.shortcuts import render, redirect
from .models import Event, EventForm, User, Category, SignInForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    events_list = Event.objects.all()
    error = ''
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                error = ''
                return HttpResponseRedirect(reverse('events:index'))
            else:
                error = 'Username or password not correct'
        else:
            form = SignInForm()
    else:
        form = SignInForm()

    context = {'events_list': events_list,
               'form': form, 'error': error}
    return render(request, 'events/index.html', context)

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('events:index'))
    else:
        form = EventForm()

    return render(request, 'events/event_form.html', {'form': form})


def logout_request(request):
    logout(request)
    return redirect('events:index')

def delete_event(request, idEvent=None):
    Event.objects.filter(id=idEvent).delete()
    return redirect('events:index')

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('inicio')
        if form.is_valid():
            print('form valido')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('events:index')
    else:
            form = UserCreationForm()

    return render(request, 'events/register_form.html', {'form': form})


def edit_event(request, idEvent=None):
    event = Event.objects.get(id=idEvent)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('events:index'))
    else:
        form = EventForm(instance=event)
        context={'form':form, 'event':event}

    return render(request, 'events/editEvent.html', context)