from django import forms
from game_app.views import GameModel




class GameForm(forms.Form):
    games = forms.ModelChoiceField(queryset=GameModel.objects.all(), label='title', to_field_name="pk")
