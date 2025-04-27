# config.py
"""
Configuration settings for the speech translation system.
"""

# Target language code (ISO 639-1)
# Examples: 'es' (Spanish), 'fr' (French), 'de' (German), 'ja' (Japanese)
TARGET_LANGUAGE = 'es'  # Default to Spanish

# Speech recognition settings
SAMPLE_RATE = 16000
RECORD_SECONDS = 5

# Model paths
VOSK_MODEL_PATH = "./models/vosk-model-small-en-us-0.15"
TRANSLATION_MODEL = "Helsinki-NLP/opus-mt-en-{}"  # Will be formatted with TARGET_LANGUAGE

# Audio settings
DEFAULT_VOICE_ID = None  # Let pyttsx3 use default voice
