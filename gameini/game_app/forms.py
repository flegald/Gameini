from django import forms
from game_app.models import GameModel


class GameForm(forms.Form):
    games = forms.ModelChoiceField(queryset=GameModel.objects.all(), label='title', to_field_name="pk")


class UploadForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = ['title', 'ini_file']

# class DynoForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         forms.Form.__init__(self, *args, **kwargs):
