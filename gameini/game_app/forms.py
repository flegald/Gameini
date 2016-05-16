"""Forms."""
from django import forms
from game_app.models import GameModel
from game_app.clean_files import separate_sections


class GameForm(forms.Form):
    """Drop down menu."""

    games = forms.ModelChoiceField(queryset=GameModel.objects.all(), label='title', to_field_name="pk")


class SectionsForm(forms.Form):
    """Drop down with ini sections."""

    def __init__(self, game_sections, *args, **kwargs):
        """Initialize drop down."""
        super(SectionsForm, self).__init__(*args, **kwargs)
        self.fields['game_sections'] = forms.ChoiceField(choices=[(section, section) for section in game_sections])


class UploadForm(forms.ModelForm):
    """Upload form."""

    class Meta:
        """Meta."""

        model = GameModel
        fields = ['title', 'ini_file']
