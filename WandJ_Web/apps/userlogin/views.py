"""
Module that for main page and user registration using forms package
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm

# Create your views here.

def Home(request):
    """
    main view where the user can see the options to text analysis
    and signup and/or login
    """
    options = [
        ('Sentiments', 'sentiments'),
        ('Classification', 'classification'),
        ('Entity', 'entities'),
        ('Concepts', 'concepts'),
        ('Summary', 'summary')
    ]
    return render(request, 'home.html', {'options': options})


def SignUp(request):
    """
    View for user registration to the app in order to use the API
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

        