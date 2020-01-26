"""WandJ_Web textAnalysis App URL Configuration
"""
from django.contrib import admin
from django.urls import path
from .views import (SentimentView,
                                    ClassificationView,
                                    EntityView,
                                    ConceptView,
                                    SummaryView)


urlpatterns = [
    path('sentiment/', SentimentView, name='sentiments'),
    path('classification/', ClassificationView, name='classification'),
    path('entity/', EntityView, name='entities'),
    path('concept/', ConceptView, name='concepts'),
    path('summary/', SummaryView, name='summary'),
]
