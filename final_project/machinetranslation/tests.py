import unittest

from translator import english_to_french, french_to_english

class test_translator(unittest.TestCase):
    def test_english_to_fench(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('Yes'),'Oui')

    def test_french_to_english(self):
        self.assertNotEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Bonjour'),'Hi')

if __name__ == "__main__":
    unittest.main()
