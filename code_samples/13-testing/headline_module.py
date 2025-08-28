# Lab 8: Headline Module
# This module contains the Headline class definition for use in other files

class Headline:
    """
    A class to represent a news headline with its source.
    
    Attributes:
        text (str): The headline text
        source (str): The news source (e.g., "BBC News")
    """
    
    def __init__(self, text, source):
        """
        Initialize a new Headline object.
        
        Args:
            text (str): The headline text
            source (str): The news source
        """
        self.text = text
        self.source = source
    
    def __str__(self):
        """
        Return a string representation of the Headline object.
        
        Returns:
            str: A readable representation of the headline
        """
        return f"Headline(text='{self.text}', source='{self.source}')"
    
    def get_word_count(self):
        """
        Get the number of words in the headline text.
        
        Returns:
            int: The word count
        """
        return len(self.text.split())
    
    def get_character_count(self):
        """
        Get the total character count of the headline text.
        
        Returns:
            int: The character count
        """
        return len(self.text)
    
    def is_long_headline(self):
        """
        Check if the headline is considered long (more than 8 words).
        
        Returns:
            bool: True if headline has more than 8 words
        """
        return self.get_word_count() > 8
    
    def contains_keyword(self, keyword):
        """
        Check if the headline contains a specific keyword.
        
        Args:
            keyword (str): The keyword to search for
            
        Returns:
            bool: True if keyword is found in headline
        """
        return keyword.lower() in self.text.lower()

    def upper(self):
        return self.text.upper()
