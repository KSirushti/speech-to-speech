"""
Main application for the offline speech translation system.
"""
import os
import sys
import time
from modules.speech_recognition import SpeechRecognizer
from modules.translator import Translator
from modules.text_to_speech import TextToSpeech
import config


def setup_directories():
    """Create necessary directories if they don't exist."""
    directories = ['models', 'audio']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")


def display_language_options():
    """Display a selection of common and Indian languages for translation."""
    languages = {
        '1': {'code': 'ar', 'name': 'Arabic'},
        '2': {'code': 'zh', 'name': 'Chinese'},
        '3': {'code': 'fr', 'name': 'French'},
        '4': {'code': 'de', 'name': 'German'},
        '5': {'code': 'hi', 'name': 'Hindi'},
        '6': {'code': 'ta', 'name': 'Tamil'},
        '7': {'code': 'te', 'name': 'Telugu'},
        '8': {'code': 'ml', 'name': 'Malayalam'},
        '9': {'code': 'kn', 'name': 'Kannada'},
        '10': {'code': 'mr', 'name': 'Marathi'},
        '11': {'code': 'gu', 'name': 'Gujarati'},
        '12': {'code': 'pa', 'name': 'Punjabi'},
        '13': {'code': 'bn', 'name': 'Bengali'},
        '14': {'code': 'ur', 'name': 'Urdu'},
        '15': {'code': 'es', 'name': 'Spanish'},
        '16': {'code': 'C', 'name': 'Custom'}
    }

    print("\n===== Available Languages =====")
    for key, lang in languages.items():
        if lang['code'] != 'C':
            print(f"{key}: {lang['name']} ({lang['code']})")
        else:
            print(f"{key}: Custom (enter your own language code)")

    while True:
        choice = input("\nSelect a language (1-16): ").strip()
        if choice in languages:
            if languages[choice]['code'] == 'C':
                custom_code = input("Enter custom language code (e.g., 'nl' for Dutch): ")
                return custom_code.strip().lower()
            else:
                return languages[choice]['code']
        else:
            print("Invalid choice. Please try again.")


def main():
    """Main function to run the speech translation system."""
    setup_directories()

    print("\n===== Offline Speech Translation System =====\n")

    # Initialize components
    try:
        speech_recognizer = SpeechRecognizer(
            model_path=config.VOSK_MODEL_PATH,
            sample_rate=config.SAMPLE_RATE
        )
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        translator = Translator(
            model_name_template=config.TRANSLATION_MODEL,
            target_lang=config.TARGET_LANGUAGE
        )
    except Exception as e:
        print(f"Failed to initialize translator: {e}")
        sys.exit(1)

    tts = TextToSpeech(voice_id=config.DEFAULT_VOICE_ID)

    # Main loop
    try:
        while True:
            print("\nOptions:")
            print("1. Translate speech (English to {})".format(config.TARGET_LANGUAGE))
            print("2. List available voices")
            print("3. Change target language")
            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ")

            if choice == '1':
                # Step 1: Speech to text
                print("\n--- Speech Recognition ---")
                text = speech_recognizer.recognize_from_microphone(
                    duration=config.RECORD_SECONDS
                )
                print(f"Recognized text: {text}")

                if not text:
                    print("No speech detected. Please try again.")
                    continue

                # Step 2: Translate text
                print("\n--- Translation ---")
                translated_text = translator.translate(text)
                print(f"Translated text: {translated_text}")

                # Step 3: Text to speech
                print("\n--- Text to Speech ---")
                tts.text_to_speech(translated_text)

                # Optionally save the audio
                save_audio = input("\nDo you want to save the audio? (y/n): ")
                if save_audio.lower() == 'y':
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    filename = f"audio/translation_{timestamp}.mp3"
                    tts.save_to_file(translated_text, filename)
                    print(f"Audio saved to {filename}")

            elif choice == '2':
                print("\n--- Available Voices ---")
                voices = tts.list_voices()
                for voice in voices:
                    print(f"ID: {voice['id']}, Name: {voice['name']}, Gender: {voice['gender']}")

                change_voice = input("\nDo you want to change the voice? (y/n): ")
                if change_voice.lower() == 'y':
                    voice_id = int(input("Enter voice ID: "))
                    if tts.set_voice(voice_id):
                        print("Voice changed successfully.")
                    else:
                        print("Invalid voice ID.")


            elif choice == '3':

                print("\n--- Change Target Language ---")

                new_lang = display_language_options()

                confirm = input(
                    f"Change target language to '{new_lang}'? This will reload the translation model. (y/n): ")

                if confirm.lower() == 'y':

                    try:

                        # Update config and reload translator

                        config.TARGET_LANGUAGE = new_lang

                        translation_model_name = config.TRANSLATION_MODEL.format(new_lang)

                        print(f"Loading new model: {translation_model_name}...")

                        translator = Translator(

                            model_name_template=config.TRANSLATION_MODEL,

                            target_lang=config.TARGET_LANGUAGE

                        )

                        print(f"Target language successfully changed to '{new_lang}'.")

                    except Exception as e:

                        print(f"Failed to load translation model for '{new_lang}':\n{e}")

            elif choice == '4':
                print("\nExiting program. Goodbye!")
                break

            else:
                print("\nInvalid choice. Please try again.")

    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())