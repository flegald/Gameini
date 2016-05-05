from django.test import TestCase
from .models import GameModel
from .forms import UploadForm
from game_app.junk_drawer import reset_file
import os


class JunkTestCase(TestCase):
    """Test junk_drawer functions."""

    def setUp(self):
        """Setup."""

    def test_reset_file(self):
        """Test Reset."""
        model = GameModel(title='test1', ini_file='ini_files/UserSettings.ini')
        file = reset_file(model.ini_file)
        self.assertIsInstance(file, str)