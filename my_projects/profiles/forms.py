from django import forms
from .models import MissingPerson, MatchingPerson

class MissingPersonForm(forms.ModelForm):
    class Meta:
        model = MissingPerson
        fields = ['name', 'age', 'gender', 'description', 'last_seen_location', 'image']  # Fields for missing persons

class MatchingPersonForm(forms.ModelForm):
    class Meta:
        model = MatchingPerson
        fields = ['name', 'age', 'gender', 'description', 'found_location', 'image']  # Fields for matching persons
