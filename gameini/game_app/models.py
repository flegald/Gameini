"""Game Model."""
from django.db import models


class GameModel(models.Model):
    """Model of Game Ini Files."""

    title = models.CharField(default='', max_length=255)
    ini_file = models.FileField(upload_to='ini_files')

    def __str__(self):
        """String representation of model."""
        return self.title
