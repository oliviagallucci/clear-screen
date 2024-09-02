import unittest
from unittest.mock import patch
from clear_screen import clear_screen

class TestClearScreen(unittest.TestCase):

    @patch('clear_screen.os.name', 'posix')
    @patch('clear_screen.os.system')
    def test_clear_screen_linux(self, mock_system):
        clear_screen()
        mock_system.assert_called_once_with('clear')

    @patch('clear_screen.os.name', 'nt')
    @patch('clear_screen.os.system')
    def test_clear_screen_windows(self, mock_system):
        clear_screen()
        mock_system.assert_called_once_with('cls')

    @patch('clear_screen.os.name', 'unknown')
    @patch('clear_screen.os.system')
    def test_clear_screen_unknown_os(self, mock_system):
        clear_screen()
        mock_system.assert_not_called()

if __name__ == '__main__':
    unittest.main()
