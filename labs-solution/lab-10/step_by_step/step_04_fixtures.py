# Lab 10: Step 4 - Using Pytest Fixtures
# This demonstrates refactoring tests to use fixtures

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

@pytest.fixture
def short_headline():
    """
    Another fixture for a short headline.
    """
    return Headline("Short", "BBC News")

@pytest.fixture
def long_headline():
    """
    Fixture for a long headline.
    """
    return Headline("This is a very long headline with many words to test functionality", "BBC News")

# Refactored tests using fixtures
def test_headline_with_fixture(sample_headline):
    """
    Test using the fixture to demonstrate fixture usage.
    """
    # Use the fixture-provided headline
    assert sample_headline.text == "This is a sample headline for testing"
    assert sample_headline.source == "BBC News"
    assert sample_headline.get_word_count() == 8

def test_short_headline_with_fixture(short_headline):
    """
    Test using the short headline fixture.
    """
    assert short_headline.text == "Short"
    assert short_headline.get_word_count() == 1

def test_long_headline_with_fixture(long_headline):
    """
    Test using the long headline fixture.
    """
    assert long_headline.text == "This is a very long headline with many words to test functionality"
    assert long_headline.get_word_count() == 15

def test_multiple_fixtures(sample_headline, short_headline):
    """
    Test using multiple fixtures in one test.
    """
    # Test sample headline
    assert sample_headline.get_word_count() == 8
    
    # Test short headline
    assert short_headline.get_word_count() == 1
    
    # Verify they're different objects
    assert sample_headline.text != short_headline.text

# Demonstrate the fixture-based tests (this would normally be run by pytest)
if __name__ == "__main__":
    print("Step 4: Using Pytest Fixtures")
    print("=" * 50)
    print("This demonstrates refactoring tests to use fixtures.")
    print("In a real test file, pytest would run these automatically.")
    print("=" * 50)
    
    try:
        # Create fixture objects manually for demonstration
        sample_headline = Headline("This is a sample headline for testing", "BBC News")
        short_headline = Headline("Short", "BBC News")
        long_headline = Headline("This is a very long headline with many words to test functionality", "BBC News")
        
        # Test the fixture-based logic
        test_headline_with_fixture(sample_headline)
        test_short_headline_with_fixture(short_headline)
        test_long_headline_with_fixture(long_headline)
        test_multiple_fixtures(sample_headline, short_headline)
        
        print("✅ All fixture-based tests passed!")
        print("✅ Code duplication reduced!")
        print("✅ Tests are more maintainable!")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    print("=" * 50)
    print("Fixtures make tests cleaner and more maintainable!")
    print("They provide consistent test data across multiple tests.")
