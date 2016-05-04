"""Tests file."""
from django.test import TestCase, Client
from .models import GameModel
from .forms import UploadForm
import factory


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
        self.client = Client()
        self.file = GameFactory.create()
        self.file1 = GameFactory.create()

    # Model Tests

    def test_game_title_works(self):
        """Assert game has title."""
        self.assertTrue(self.file.title)

    def test_game_file_works(self):
        """Assert game has file."""
        self.assertTrue(self.file.ini_file)

    def test_in_db(self):
        """Assert files in DB."""
        self.assertEqual(len(GameModel.objects.all()), 2)

    # View Tests

    def test_home_view_get(self):
        """Test home view."""
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_home_view_post(self):
        """Test home view post."""
        form = UploadForm(self.client.post())
        response = self.client.post(
            '/files/{}'.format(self.file.id),
            follow=True
        )
        self.assertEqual()

    def test_upload_view(self):
        """Test upload view."""
        response = self.client.post(
            '/files/upload',
            {'title': self.file.title,
                'ini_file': self.file.ini_file},
            follow=True
        )
        self.assertEqual(response[0], '/generateform/{}'.format(self.file.id))




