"""
Solution for Lab 10: Automated Testing with Pytest.
"""

import pytest
from headline_module import Headline

# Step 4: Refactor with a Fixture
@pytest.fixture
def sample_headline():
    """A sample Headline object for use in tests."""
    return Headline("This is the fixture text", "Fixture Source")


# Step 2: Write a Basic Test
def test_headline_creation():
    """
    Tests the basic creation of a Headline object without using a fixture.
    """
    h = Headline("A regular headline", "A regular source")
    assert h.text == "A regular headline"
    assert h.source == "A regular source"


# Step 3: Test a Method
def test_get_word_count():
    """
    Tests the get_word_count method without using a fixture.
    """
    h = Headline("This headline has exactly five words", "Test Source")
    assert h.get_word_count() == 5


# You can also test edge cases, like empty strings
def test_get_word_count_empty():
    """Tests the get_word_count method with an empty string."""
    h = Headline("", "Test Source")
    assert h.get_word_count() == 0


# This test uses the fixture defined above.
# Pytest automatically creates the sample_headline and passes it in.
def test_headline_creation_with_fixture(sample_headline):
    """
    Tests the attributes of the headline provided by the fixture.
    """
    assert sample_headline.text == "This is the fixture text"
    assert sample_headline.source == "Fixture Source"

def test_get_word_count_with_fixture(sample_headline):
    """
    Tests the get_word_count method of the headline from the fixture.
    """
    # The text "This is the fixture text" has 5 words.
    assert sample_headline.get_word_count() == 5 