# """Tests file."""
# from django.test import TestCase, Client
# from .models import GameModel
# from .forms import UploadForm
# import factory
# import os
# from django.core.files.uploadedfile import SimpleUploadedFile


# class GameTestCase(TestCase):
#     """Test Game model."""

#     def setUp(self):
#         """Setup."""
#         self.client = Client()
#         self.file = GameModel(title='grass cutters 3', ini_file='ini_files/settings.ini')
#         self.file.save()

    # Model Tests

    # def test_game_title_works(self):
    #     """Assert game has title."""
    #     self.assertTrue(self.file.title)

    # def test_game_file_works(self):
    #     """Assert game has file."""
    #     self.assertTrue(self.file.ini_file)

    # def test_in_db(self):
    #     """Assert files in DB."""
    #     self.assertEqual(len(GameModel.objects.all()), 1)

    # # View Tests

    # def test_home_view_get(self):
    #     """Test home view."""
    #     self.assertEqual(self.client.get('/').status_code, 200)

    # def test_upload_view_post(self):
    #     """Test upload view post."""

    #     file = GameModel(title='grass cutters 4', ini_file='ini_files/settings.ini')

    #     response = self.client.post(

    #         '/files/upload',
    #         {'title': file.title, 'ini_file': file.ini_file},
    #         format='multipart',
    #         follow=True
    #     )

    #     file = GameModel.objects.get(title='grass cutters 4')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertRedirects(response, '/generateform/{}'.format(file.id), status_code=302)

    # def test_upload_view(self):
    #     """Test upload view."""
    #     response = self.client.post(
    #         '/files/upload',
    #         {'title': self.file.title,
    #             'ini_file': self.file.ini_file},
    #         follow=True
    #     )
    #     import pdb; pdb.set_trace()
    #     self.assertEqual(response[0], '/generateform/{}'.format(self.file.id))

    # def test_generate_form(self):
    #     """Test Generate Form."""
    #     response = self.client.post('/generateform/{}'.format(self.file.id), self.file.ini_file)
    #     self.assertEqual(self.client.get(response.status_code, 200))
