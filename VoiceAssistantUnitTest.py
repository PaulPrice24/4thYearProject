import unittest
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from unittest.mock import MagicMock, patch
from io import StringIO
import sys
import datetime
import speech_recognition as sr
import pygetwindow as gw
import sounddevice as sd
import azure.cognitiveservices.speech as speechsdk
from datetime import datetime
from phue import Bridge, PhueRequestTimeout
from ip_address import bridge_ip_address

class TestVoiceAssistant(unittest.TestCase):
    
    @patch('sys.argv', ['test_name', '01/01/2000'])
    @patch('builtins.input', side_effect=['dummy command'])
    @patch('builtins.print', side_effect=lambda *args: None)
    def test_speech_recognition_and_command_parsing(self, mock_print, mock_input):
        from main import main

        with patch('speech_recognition.Recognizer.recognize_once') as mock_recognize_once:
            mock_recognize_once.return_value.text = "dummy command"
            captured_output = StringIO()
            sys.stdout = captured_output
            main(None, None)
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip()
            self.assertIn('The input speech was: dummy command', output)
    
    def test_text_to_speech_functionality(self):

        from main import speak

        captured_output = StringIO()
        sys.stdout = captured_output

        speak("This is a test.")

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        self.assertEqual(output, "This is a test.")
    
    @patch('webbrowser.get')
    def test_opening_web_pages(self, mock_webbrowser_get):
        from main import main

        mock_webbrowser_get.return_value.open_new.side_effect = MagicMock()

        main('test_name', '01/01/2000')

        mock_webbrowser_get.assert_called_with('chrome')

    @patch('os.system')

    def test_playing_music(self, mock_os_system):
        from main import main

        mock_os_system.side_effect = MagicMock()

        main('test_name', '01/01/2000')

        mock_os_system.assert_called_with("spotify")
    
    @patch('phue.Bridge.set_light')
    def test_controlling_lights(self, mock_bridge_set_light):
        from main import main

        mock_bridge_set_light.side_effect = MagicMock()

        main('test_name', '01/01/2000')

        mock_bridge_set_light.assert_called_with('Champs room', 'on', True)
    
    @patch('pyautogui.hotkey')
    def test_controlling_keyboard_actions(self, mock_pyautogui_hotkey):
        from main import main

        mock_pyautogui_hotkey.side_effect = MagicMock()

        main('test_name', '01/01/2000')

        mock_pyautogui_hotkey.assert_called_with('win', 's')

    @patch('pyautogui.hotkey')
    def test_opening_and_terminating_applications(self, mock_pyautogui_hotkey):
        from main import main

        mock_pyautogui_hotkey.side_effect = MagicMock()

        main('test_name', '01/01/2000')

        mock_pyautogui_hotkey.assert_called_with('win', 's')

if __name__ == '__main__':
    with open('voice_assistant_unit_test_results.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)