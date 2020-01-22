"""
Module to get the different results of the API endpoints
"""

from django.shortcuts import render, redirect
from aylienapiclient import textapi
from django.http import JsonResponse

from .forms import (SentimentsForm,
                    ClassificationForm,
                    EntitiesForm,
                    ConceptsForm,
                    SummarizeForm)
from .credentials import credentials

import json
import sys

# Create your views here.

# Creating the client object with the ID and KEY of the user. Using python SDK's textapi
client = textapi.Client(credentials['id'], credentials['key'])



def SentimentView(request):
    """
    Method that makes the request to the API endpoint 'sentiment' with the parameters needed,
    and show the results.
    """
    if request.method == "POST":
        form = SentimentsForm(request.POST)
        if form.is_valid():
            inputText = form.cleaned_data.get('inputText')
            if inputText.startswith( 'http' ):
                param1 = 'url'
            else:
                param1 = 'text'
            mode = form.cleaned_data.get('mode')
            language = form.cleaned_data.get('language')
            dictSentiments = {param1: inputText, 'mode': mode,'language': language}          
            sentiment = client.Sentiment(dictSentiments)
            sentimentList = [ (k,json.dumps(v)) for k, v in sentiment.items() ]
            return render(request, 'sentiments.html',  {'data':sentimentList, 'form': form, 'text':sentiment['text']})
    else:
        form = SentimentsForm()
    return render(request, 'sentiments.html', {'form': form})


def ClassificationView(request):
    """
    Method that makes the request to the API endpoint 'classify' with the parameters needed,
    and show the results.
    """
    if request.method == "POST":
        form = ClassificationForm(request.POST)
        if form.is_valid():
            inputText = form.cleaned_data.get('inputText')
            if inputText.startswith( 'http' ):
                param1 = 'url'
            else:
                param1 = 'text'
            taxonomy = form.cleaned_data.get('taxonomy')
            language = form.cleaned_data.get('language')
            dictClassification = {param1: inputText, 'taxonomy': taxonomy,'language': language}          
            classification = client.Classify(dictClassification)
            return render(request, 'classification.html',  {'data':classification, 'form': form, 'categories': classification['categories'][0]})
    else:
        form = ClassificationForm()
    return render(request, 'classification.html', {'form': form})


def EntityView(request):
    """
    Method that makes the request to the API endpoint 'Entity' with the parameters needed,
    and show the results.
    """
    if request.method == "POST":
        form = EntitiesForm(request.POST)
        if form.is_valid():
            inputText = form.cleaned_data.get('inputText')
            if inputText.startswith( 'http' ):
                param1 = 'url'
            else:
                param1 = 'text'
            language = form.cleaned_data.get('language')
            dictEntities = {param1: inputText, 'language': language}          
            entities = client.Entities(dictEntities)
            return render(request, 'entities.html',  {'data':entities, 'form': form, 'entities': entities['entities']})
    else:
        form = EntitiesForm()
    return render(request, 'entities.html', {'form': form})

def ConceptView(request):
    """
    Method that makes the request to the API endpoint 'Concept' with the parameters needed,
    and show the results.
    """
    if request.method == "POST":
        form = ConceptsForm(request.POST)
        if form.is_valid():
            inputText = form.cleaned_data.get('inputText')
            if inputText.startswith( 'http' ):
                param1 = 'url'
            else:
                param1 = 'text'
            language = form.cleaned_data.get('language')
            dictConcepts = {param1: inputText, 'language': language}          
            concepts = client.Concepts(dictConcepts)
            conceptsList = [ v for v in concepts['concepts'].values() ]
            return render(request, 'concepts.html',  {'data':concepts, 'form': form, 'concepts': conceptsList})
    else:
        form = ConceptsForm()
    return render(request, 'concepts.html', {'form': form})


def SummaryView(request):
    """
    Method that makes the request to the API endpoint 'Summarize' with the parameters needed,
    and show the results.
    """
    print("REQUEST: ", request)
    if request.method == "POST":
        form = SummarizeForm(request.POST)
        if form.is_valid():
            print("FORM: ", form)
            inputText = form.cleaned_data.get('inputText')
            if inputText.startswith( 'http' ):
                param1 = 'url'
            else:
                param1 = 'text'
            number = form.cleaned_data.get('number')
            language = form.cleaned_data.get('language')
            dictSummary = {param1: inputText, 'sentences_number': number,'language': language}          
            summary = client.Summarize(dictSummary)
            return render(request, 'summary.html',  {'data':summary, 'form': form, 'sentences': summary['sentences']})
    else:
        form = SummarizeForm()
    return render(request, 'summary.html', {'form': form})