# modules/text_to_speech.py
"""
Module for text-to-speech conversion using pyttsx3.
"""
import pyttsx3


class TextToSpeech:
    def __init__(self, voice_id=None):
        """Initialize the TTS engine."""
        self.engine = pyttsx3.init()

        if voice_id:
            self.engine.setProperty('voice', voice_id)

        # Get list of available voices
        self.voices = self.engine.getProperty('voices')

    def list_voices(self):
        """List all available voices."""
        voices_info = []
        for i, voice in enumerate(self.voices):
            voices_info.append({
                'id': i,
                'name': voice.name,
                'languages': voice.languages,
                'gender': voice.gender,
                'age': voice.age
            })
        return voices_info

    def set_voice(self, voice_id):
        """Set the voice by ID."""
        if 0 <= voice_id < len(self.voices):
            self.engine.setProperty('voice', self.voices[voice_id].id)
            return True
        return False

    def text_to_speech(self, text):
        """Convert text to speech and play it."""
        if not text.strip():
            print("No text to speak.")
            return

        print(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def save_to_file(self, text, file_path):
        """Save speech to an audio file."""
        if not text.strip():
            print("No text to save.")
            return

        self.engine.save_to_file(text, file_path)
        self.engine.runAndWait()