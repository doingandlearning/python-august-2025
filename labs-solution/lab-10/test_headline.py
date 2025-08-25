# Lab 10: Automated Testing with Pytest - Complete Solution
# This file contains all the tests for the Headline class

import pytest
from headline_module import Headline

# Step 4: Fixture for common test data
@pytest.fixture
def sample_headline():
    """
    Fixture that provides a standard Headline object for testing.
    This reduces code duplication across multiple tests.
    """
    return Headline("This is a sample headline for testing", "BBC News")

# Step 2: Basic test for object creation
def test_headline_creation():
    """
    Test that Headline objects are created correctly with the right attributes.
    """
    # Create a Headline instance with test data
    headline = Headline("General election: Labour and Tories clash over tax", "BBC News")
    
    # Assert that attributes are set correctly
    assert headline.text == "General election: Labour and Tories clash over tax"
    assert headline.source == "BBC News"

# Step 3: Test for the get_word_count method
def test_get_word_count():
    """
    Test that the get_word_count method returns the correct word count.
    """
    # Create a Headline with known word count
    headline = Headline("This has four words", "BBC News")
    
    # Assert that the method returns the expected count
    assert headline.get_word_count() == 4

# Additional test using the fixture
def test_headline_with_fixture(sample_headline):
    """
    Test using the fixture to demonstrate fixture usage.
    """
    # Use the fixture-provided headline
    assert sample_headline.text == "This is a sample headline for testing"
    assert sample_headline.source == "BBC News"
    assert sample_headline.get_word_count() == 8

# Additional tests for comprehensive coverage
def test_empty_headline():
    """
    Test edge case: empty headline text.
    """
    headline = Headline("", "BBC News")
    assert headline.get_word_count() == 0
    assert headline.text == ""
    assert headline.source == "BBC News"

def test_single_word_headline():
    """
    Test edge case: single word headline.
    """
    headline = Headline("Breaking", "BBC News")
    assert headline.get_word_count() == 1
    assert headline.text == "Breaking"

def test_long_headline():
    """
    Test edge case: longer headline with multiple words.
    """
    headline = Headline("This is a very long headline with many words to test the word counting functionality", "BBC News")
    assert headline.get_word_count() == 15

def test_headline_with_punctuation():
    """
    Test that punctuation doesn't affect word counting.
    """
    headline = Headline("Breaking news: Major announcement!", "BBC News")
    assert headline.get_word_count() == 3

def test_headline_string_representation():
    """
    Test the __str__ method of the Headline class.
    """
    headline = Headline("Test headline", "Test Source")
    expected_string = "Headline(text='Test headline', source='Test Source')"
    assert str(headline) == expected_string

def test_headline_contains_keyword():
    """
    Test the contains_keyword method if it exists in the Headline class.
    """
    headline = Headline("Climate change affects global temperatures", "BBC News")
    
    # Test with existing keyword
    assert headline.contains_keyword("climate") == True
    assert headline.contains_keyword("Climate") == True
    
    # Test with non-existing keyword
    assert headline.contains_keyword("politics") == False

def test_headline_is_long_headline():
    """
    Test the is_long_headline method if it exists in the Headline class.
    """
    # Test short headline
    short_headline = Headline("Short", "BBC News")
    assert short_headline.is_long_headline() == False
    
    # Test long headline
    long_headline = Headline("This is a very long headline that should be considered long", "BBC News")
    assert long_headline.is_long_headline() == True

if __name__ == "__main__":
    # This allows running the file directly for demonstration
    print("Lab 10: Automated Testing with Pytest")
    print("=" * 50)
    print("This file contains tests for the Headline class.")
    print("Run with: pytest test_headline.py")
    print("=" * 50)
