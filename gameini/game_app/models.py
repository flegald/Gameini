from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class GameModel(models.Model):
    """Model of Game Ini Files."""

    title = models.CharField(default='', max_length=255)
    ini_file = models.FileField(upload_to='ini_files')
