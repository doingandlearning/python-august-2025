"""
Solution for the Modules Lab: The Headline Module.

This file contains the definition for the Headline class.
It is intended to be imported by other scripts.
"""

class Headline:
    """A class to represent a single news headline and its source."""

    def __init__(self, text, source):
        """Initializes a Headline object."""
        self.text = text
        self.source = source

    def __repr__(self):
        """Returns an unambiguous string representation of the object."""
        return f"Headline(text='{self.text}', source='{self.source}')"

    def get_word_count(self):
        """Returns the number of words in the headline's text."""
        return len(self.text.split()) 