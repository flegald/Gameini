"""Forms."""
from django import forms
from game_app.views import GameModel


class GameForm(forms.Form):
    """Drop down menue."""

    games = forms.ModelChoiceField(queryset=GameModel.objects.all(), label='title', to_field_name="pk")


class UploadForm(forms.ModelForm):
    """Upload form."""

    class Meta:
        """Meta."""

        model = GameModel
        fields = ['title', 'ini_file']


class DynoForm(forms.Form):
    """Dynamically generated form."""

    def __init__(self, *args, **kwargs):
        """Init."""
        forms.Form.__init__(self, *args, **kwargs)
        self.name = forms.CharField(label='something', max_length=100, initial=kwargs['initial']['first run'])
        # import pdb; pdb.set_trace()
        # for key in kwargs['initial']:
        #     self.name = forms.CharField(
        #         label=kwargs['initial'],
        #         max_length=100,
        #         initial=kwargs['initial'][key]
        #     )

