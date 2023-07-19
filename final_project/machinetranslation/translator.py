'''This module contains functions for my translator'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''This function translates English text to French text'''
    text = MyMemoryTranslator(source= 'en-US', target= 'fr-FR')
    french_text = text.translate(english_text)
    return french_text


def french_to_english(french_text):
    '''This function translates French text to English text'''
    text = MyMemoryTranslator(source= 'fr-FR', target= 'en-US')
    french_text = text.translate(french_text)
    return french_text
