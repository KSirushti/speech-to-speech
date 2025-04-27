# Offline Speech Translation System

A Python-based application that allows users to speak in English and get real-time translations in multiple languages with audio output. This system works offline after initial setup.

## Features

- **Speech Recognition**: Convert spoken English to text
- **Translation**: Translate English text into multiple languages
- **Text-to-Speech**: Convert translated text to spoken audio
- **Language Selection**: Support for numerous languages
- **Voice Selection**: Choose from available system voices
- **Audio Saving**: Option to save translations as audio files

## Prerequisites

- Python 3.x (Tested with Python 3.12-3.13)
- Windows, macOS, or Linux operating system
- Microphone for speech input
- Speakers for audio output

## Installation

1. Clone or download this repository to your local machine.

2. Create necessary directories:
   ```
   mkdir -p models audio modules
   ```

3. Install required dependencies:
   ```
   pip install vosk==0.3.45
   pip install sounddevice==0.4.6
   pip install numpy==1.24.3
   pip install googletrans==4.0.0-rc1
   pip install pyttsx3==2.90
   ```

4. Download the Vosk speech recognition model:
   - Visit [Vosk Models](https://alphacephei.com/vosk/models)
   - Download the small English model (vosk-model-small-en-us-0.15)
   - Extract the zip file
   - Move the extracted folder to the `models` directory

## Project Structure

```
speech_translator/
├── __init__.py
├── main.py               # Main application entry point
├── config.py             # Configuration settings
├── models/               # Directory for speech recognition models
│   └── vosk-model-small-en-us-0.15/
├── audio/                # Directory for saved audio files
├── requirements.txt      # Python dependencies
└── modules/
    ├── __init__.py
    ├── speech_recognition.py  # Speech-to-text module
    ├── translator.py          # Text translation module
    └── text_to_speech.py      # Text-to-speech module
```

## Usage

1. Run the main script:
   ```
   python main.py
   ```

2. Use the menu options:
   - **Option 1**: Translate speech from English to the selected language
   - **Option 2**: List and change available voice options
   - **Option 3**: Change the target language
   - **Option 4**: Exit the program

3. When translating:
   - Speak clearly in English when prompted
   - The system will display the recognized text and its translation
   - The translation will be spoken aloud
   - You can choose to save the audio file

## Supported Languages

The system supports translation to numerous languages, including but not limited to:
- Spanish (es)
- French (fr)
- German (de)
- Chinese (zh)
- Japanese (ja)
- Russian (ru)
- Tamil (ta)
- Hindi (hi)
- Italian (it)
- Portuguese (pt)
- Arabic (ar)

## Customization

You can easily customize the system by editing the `config.py` file:

```python
# Target language code (ISO 639-1)
TARGET_LANGUAGE = 'es'  # Change to your preferred default language

# Speech recognition settings
SAMPLE_RATE = 16000
RECORD_SECONDS = 5  # Adjust recording duration as needed
```

## Troubleshooting

- **No audio input detected**: Check your microphone settings and permissions
- **Speech recognition issues**: Try speaking more clearly or increase recording time
- **Translation problems**: Verify that the language code is correct
- **Audio output issues**: Check your system's audio settings and speakers

## License

This project is open source and available under the MIT License.

## Acknowledgements

- [Vosk](https://alphacephei.com/vosk/) for offline speech recognition
- [googletrans](https://pypi.org/project/googletrans/) for translation
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech conversion
