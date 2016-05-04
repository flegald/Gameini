"""Tests file."""
from django.test import TestCase
from .models import GameModel
import factory


# Model Tests

class GameFactory(factory.django.DjangoModelFactory):
    """Create test game model."""

    class Meta:
        """Meta."""

        model = GameModel

    title = factory.sequence(lambda n: 'title{}'.format(n))
    ini_file = factory.django.FileField(filename='ini_files/settings.ini')


class GameTestCase(TestCase):
    """Test Game model."""

    def setUp(self):
        """Setup."""
        self.file = GameFactory.create()
        self.file1 = GameFactory.create()

    def test_game_title_works(self):
        """Assert game has title."""
        self.assertTrue(self.file.title)

    def test_game_file_works(self):
        """Assert game has file."""
        self.assertTrue(self.file.ini_file)

    def test_in_db(self):
        """Assert files in DB."""
        self.assertEqual(len(GameModel.objects.all()), 2)








