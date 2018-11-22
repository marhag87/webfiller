"""Unit tests for Webfiller"""
from unittest import TestCase
import mock
from webfiller import Webfiller


class TestPasswordCleanup(TestCase):
    """Tests for Webfiller.password_cleanup"""
    def setUp(self):
        self.mock_config = mock.patch('webfiller.config').start()

    def test_starts_with_apostrophe(self):
        """Test that password cleans up when it starts with an apostrophe"""
        self.assertEqual(
            Webfiller().password_cleanup("""'aaaaa"""),
            """"'"'aaaaa'""",
        )

    def test_ends_with_apostrophe(self):
        """Test that password cleans up when it ends with an apostrophe"""
        self.assertEqual(
            Webfiller().password_cleanup("""aaaaa'"""),
            ''''aaaaa'"'"''',
        )

    def test_middle_apostrophe(self):
        """Test that password cleans up when it has an apostrophe in the middle"""
        self.assertEqual(
            Webfiller().password_cleanup("""aa'aa"""),
            """'aa'"'"'aa'""",
        )

    def test_no_apostrophe(self):
        """Test that password cleans up when it has no apostrophes"""
        self.assertEqual(
            Webfiller().password_cleanup('aaaaa'),
            "'aaaaa'",
        )

    def test_multiline_password(self):
        """Test that multiline passwords only print the first line"""
        self.assertEqual(
            Webfiller().password_cleanup("aaaa\nbbbb\ncccc"),
            "'aaaa'",
        )
