from django.shortcuts import render, redirect
from aylienapiclient import textapi
from django.http import JsonResponse

from .forms import (SentimentsForm,
                    ClassificationForm,
                    EntitiesForm,
                    ConceptsForm,
                    SummarizeForm)

import json
import sys

# Create your views here.


client = textapi.Client('6694e47d', 'c2fa32a8cd49f0eca168d4d0dc9c7c25')



def SentimentView(request):
    """
    """
    print("REQUEST: ", request)
    if request.method == "POST":
        form = SentimentsForm(request.POST)
        if form.is_valid():
            print("FORM: ", form)
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
            return render(request, 'sentiments.html',  {'data':sentimentList, 'form': form})
    else:
        form = SentimentsForm()
    return render(request, 'sentiments.html', {'form': form})


def ClassificationView(request):
    """
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
            print(classification['categories'][0].keys())
            return render(request, 'classification.html',  {'data':classification, 'form': form, 'categories': classification['categories'][0]})
    else:
        form = ClassificationForm()
    return render(request, 'classification.html', {'form': form})


def EntityView(request):
    """
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
            #entitiesList = [ (k,json.dumps(v)) for k, v in entities.items() ]
            return render(request, 'entities.html',  {'data':entities, 'form': form, 'entities': entities['entities']})
    else:
        form = EntitiesForm()
    return render(request, 'entities.html', {'form': form})

def ConceptView(request):
    """
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
            print(conceptsList)
            return render(request, 'concepts.html',  {'data':concepts, 'form': form, 'concepts': conceptsList})
    else:
        form = ConceptsForm()
    return render(request, 'concepts.html', {'form': form})


def SummaryView(request):
    """
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
            #summaryList = [ (k,json.dumps(v)) for k, v in summary.items() ]
            return render(request, 'summary.html',  {'data':summary, 'form': form, 'sentences': summary['sentences']})
    else:
        form = SummarizeForm()
    return render(request, 'summary.html', {'form': form})