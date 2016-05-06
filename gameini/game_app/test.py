"""Tests Views and Model."""
from django.test import TestCase, Client
from .models import GameModel


class GameTestCase(TestCase):
    """Test Game model."""

    def setUp(self):
        """Setup."""
        self.client = Client()
        self.file = GameModel(
            title='grass cutters 3',
            ini_file='ini_files/settings.ini'
        )
        self.file.save()

    # Model Tests

    def test_game_title_works(self):
        """Assert game has title."""
        self.assertTrue(self.file.title)

    def test_game_file_works(self):
        """Assert game has file."""
        self.assertTrue(self.file.ini_file)

    def test_in_db(self):
        """Assert file in DB."""
        self.assertEqual(len(GameModel.objects.all()), 1)

    # Home View tests

    def test_home_view_get(self):
        """Test home view with GET request."""
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_home_view_post(self):
        """Test home view with POST request."""
        file = GameModel(
            title='grass cutters 5',
            ini_file='ini_files/settings.ini'
        )
        file.save()
        key = file.pk
        response = self.client.post(
            '/',
            {'games': key}
        )
        self.assertRedirects(response, '/generateform/{}'.format(key), status_code=302)

    # Upload View test

    def test_upload_view_post(self):
        """Test upload view post."""
        file = GameModel(title='grass cutters 4', ini_file='ini_files/settings.ini')
        response = self.client.post(
            '/files/upload',
            {'title': file.title, 'ini_file': file.ini_file},
            format='multipart',
            follow=True
        )
        file = GameModel.objects.get(title='grass cutters 4')
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/generateform/{}'.format(file.id), status_code=302)

    # Generate Form View test

    def test_generate_form_with_download(self):
        """Test that a file is handed back to the user as a download."""
        file = GameModel(title='grass cutters 4', ini_file='ini_files/settings.ini')
        file.save()
        response = self.client.post('/generateform/{}'.format(file.pk))
        self.assertEqual(response.get('Content-Disposition'), "attachment; filename={}.ini".format(file.title))

