# Lab 10: Step 3 - Test for the get_word_count Method
# This demonstrates testing a class method

from headline_module import Headline

def test_get_word_count():
    """
    Test that the get_word_count method returns the correct word count.
    This is the test for Step 3.
    """
    # Create a Headline with known word count
    headline = Headline("This has four words", "BBC News")
    
    # Assert that the method returns the expected count
    assert headline.get_word_count() == 4
    
    print("✅ Method test for get_word_count completed successfully!")

def test_get_word_count_edge_cases():
    """
    Test edge cases for the get_word_count method.
    """
    # Test empty headline
    empty_headline = Headline("", "BBC News")
    assert empty_headline.get_word_count() == 0
    
    # Test single word
    single_word = Headline("Breaking", "BBC News")
    assert single_word.get_word_count() == 1
    
    # Test longer headline
    long_headline = Headline("This is a very long headline with many words", "BBC News")
    assert long_headline.get_word_count() == 10
    
    print("✅ Edge case tests for get_word_count completed successfully!")

# Demonstrate the tests (this would normally be run by pytest)
if __name__ == "__main__":
    print("Step 3: Test for the get_word_count Method")
    print("=" * 50)
    print("This demonstrates testing a class method.")
    print("In a real test file, pytest would run these automatically.")
    print("=" * 50)
    
    try:
        test_get_word_count()
        test_get_word_count_edge_cases()
        print("✅ All method tests passed! get_word_count works correctly.")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    print("=" * 50)
    print("Next step: Refactor tests to use pytest fixtures.")
