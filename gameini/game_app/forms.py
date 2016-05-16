"""Forms."""
from django import forms
from game_app.models import GameModel


class GameForm(forms.Form):
    """Drop down menu."""

    games = forms.ModelChoiceField(queryset=GameModel.objects.all(), label='title', to_field_name="pk")


class UploadForm(forms.ModelForm):
    """Upload form."""

    class Meta:
        """Meta."""

        model = GameModel
        fields = ['title', 'ini_file']
