from django import forms
from game_app.views import GameModel




class GameForm(forms.Form):
    games = forms.ModelChoiceField(queryset=GameModel.objects.all(), label='title', to_field_name="pk")


class UploadForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = ['title', 'ini_file']