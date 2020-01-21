from django import forms
from django.contrib.auth.models import User

MODES = (
    ("document", "Document") ,
    ("tweet", "Short Text"),
)
LANGUAGES = (
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("de", "German"),
    ("auto", "Auto")
)

TAXONOMY = (
    ("iptc-subjectcode", "IPTC Subject Codes"),
    ("iab-qag", "IAB QAG"),

)

LENGTH = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)
class SentimentsForm(forms.Form):
    """
    """
    inputText = forms.CharField(label='Input', max_length=500, widget=forms.Textarea(attrs={'cols': 16, 'rows': 2}))
    mode = forms.ChoiceField(choices = MODES, label="Mode", widget=forms.Select(), required=True)
    language = forms.ChoiceField(choices = LANGUAGES, label="Language", required=True)
    class Meta:
        model = User
        fields =('Input',
                'Mode',
                'Language')

class ClassificationForm(forms.Form):
    """
    """
    inputText = forms.CharField(label='Input', max_length=500)
    taxonomy = forms.ChoiceField(choices = TAXONOMY, label="Taxonomy", initial='', widget=forms.Select(), required=True)
    language = forms.ChoiceField(choices = LANGUAGES, label="Language", required=True)
    class Meta:
        model = User
        fields =('Input',
                'Taxonomy',
                'Language')

class EntitiesForm(forms.Form):
    """
    """
    inputText = forms.CharField(label='Input', max_length=500)
    language = forms.ChoiceField(choices = LANGUAGES, label="Language", required=True)
    class Meta:
        model = User
        fields =('Input',
                 'Language')

class ConceptsForm(forms.Form):
    """
    """
    inputText = forms.CharField(label='Input', max_length=500)
    language = forms.ChoiceField(choices = LANGUAGES, label="Language", required=True)
    class Meta:
        model = User
        fields =('Input',
                 'Language')

class SummarizeForm(forms.Form):
    """
    """
    inputText = forms.CharField(label='Input', max_length=500, widget=forms.Textarea(attrs={'cols': 16, 'rows': 2}))
    number = forms.ChoiceField(choices = LENGTH, label="Summary length (number of sentences)", initial=5, widget=forms.Select(), required=True)
    language = forms.ChoiceField(choices = LANGUAGES, label="Language", required=True)
    class Meta:
        model = User
        fields =('Input',
                'number',
                'Language')