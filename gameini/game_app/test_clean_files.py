from django.test import TestCase
from .models import GameModel
from game_app.junk_drawer import reset_file, config_section_map, change_settings
import io


class JunkTestCase(TestCase):
    """Test junk_drawer functions."""

    def setUp(self):
        """Setup."""
        self.model = GameModel(title='test1', ini_file='ini_files/UserSettings.ini')

    def test_reset_file_is_str(self):
        """Test reset file produces a str object."""
        file = reset_file(self.model.ini_file)
        self.assertIsInstance(file, str)

    def test_rest_file_is_at_begining(self):
        """Test file has a length greater than 0."""
        file = reset_file(self.model.ini_file)
        self.assertGreater(len(file), 0)

    def test_config_section_map(self):
        """Test Config section map."""
        parsed_dict = config_section_map(self.model.ini_file)
        # Assert first part of return is dict of file contents.
        self.assertIsInstance(parsed_dict[0], dict)
        # Assert second part retrun is str of file section.
        self.assertIsInstance(parsed_dict[1], str)

    def test_change_settings(self):
        """Test change_settings function changes a setting in file."""
        with io.FileIO('foobar.ini', 'wb+') as file:
            file.write(b'[Settings] zero_one=0')
            file.seek(0)
            self.assertEquals(file.read(), b'[Settings] zero_one=0')
            new_data = {'zero_one': '1'}
            file.seek(0)
            new_file = change_settings('Settings', new_data, file)
            new_file.seek(0)
            self.assertIn('zero_one = 1', new_file.read())
