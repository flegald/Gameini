from django.test import TestCase
from .models import GameModel
from game_app.junk_drawer import reset_file, config_section_map


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
        # import pdb; pdb.set_trace()
        self.assertIsInstance(parsed_dict[0], dict)
        self.assertIsInstance(parsed_dict[1], str)
