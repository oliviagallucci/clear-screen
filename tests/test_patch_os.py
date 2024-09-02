import unittest
from unittest.mock import patch
from clear_screen import clear_screen

class TestClearScreen(unittest.TestCase):

    @patch('your_module.os.name', 'posix')
    @patch('your_module.os.system')
    def test_clear_screen_linux(self, mock_system):
        clear_screen()
        mock_system.assert_called_once_with('clear')

    @patch('your_module.os.name', 'nt')
    @patch('your_module.os.system')
    def test_clear_screen_windows(self, mock_system):
        clear_screen()
        mock_system.assert_called_once_with('cls')

    @patch('your_module.os.name', 'unknown')
    @patch('your_module.os.system')
    def test_clear_screen_unknown_os(self, mock_system):
        clear_screen()
        mock_system.assert_not_called()

if __name__ == '__main__':
    unittest.main()
