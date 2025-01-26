# tests/test_speech.py
from modules.speech import speak, take_command

def test_speak():
    speak("This is a test.")

def test_take_command():
    command = take_command()
    assert isinstance(command, str)