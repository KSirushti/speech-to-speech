# modules/speech_recognition.py
"""
Module for speech recognition using Vosk.
"""
import json
import numpy as np
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import os


class SpeechRecognizer:
    def __init__(self, model_path, sample_rate=16000):
        # Check if model exists, if not, notify user to download it
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Vosk model not found at {model_path}. "
                f"Please download a model from https://alphacephei.com/vosk/models "
                f"and extract it to {model_path}"
            )

        self.model = Model(model_path)
        self.sample_rate = sample_rate
        self.recognizer = KaldiRecognizer(self.model, sample_rate)

    def record_audio(self, duration=5):
        """Record audio from microphone for the specified duration."""
        print(f"Recording for {duration} seconds... Speak now.")

        audio_data = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype=np.int16
        )
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")
        return audio_data

    def audio_to_text(self, audio_data):
        """Convert audio data to text using Vosk."""
        self.recognizer.AcceptWaveform(audio_data.tobytes())
        result = json.loads(self.recognizer.FinalResult())
        return result.get("text", "")

    def recognize_from_microphone(self, duration=5):
        """Record audio from microphone and convert to text."""
        audio_data = self.record_audio(duration)
        return self.audio_to_text(audio_data)

