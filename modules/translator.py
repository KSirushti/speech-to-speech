# modules/translator.py
"""
Module for text translation using offline Hugging Face models.
"""
from transformers import MarianMTModel, MarianTokenizer


class Translator:
    def __init__(self, model_name_template, target_lang):
        """Initialize the translator with the specified target language."""
        self.target_lang = target_lang
        model_name = model_name_template.format(target_lang)

        print(f"Loading translation model {model_name}...")
        try:
            self.tokenizer = MarianTokenizer.from_pretrained(model_name)
            self.model = MarianMTModel.from_pretrained(model_name)
            print("Translation model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            print(f"Please ensure you have an internet connection for the initial model download.")
            raise

    def translate(self, text):
        """Translate English text to the target language."""
        if not text.strip():
            return ""

        # Prepare the text for translation
        batch = self.tokenizer([text], return_tensors="pt", padding=True)

        # Generate translation
        translated = self.model.generate(**batch)

        # Decode the generated tokens
        result = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return result

