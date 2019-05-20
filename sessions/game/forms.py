from django import forms
from .views import MIN_VALUE, MAX_VALUE


class GameForm(forms.Form):
    value = forms.IntegerField(min_value=MIN_VALUE, max_value=MAX_VALUE)
