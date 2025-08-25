# Lab 10: Step 2 - Basic Test for Object Creation
# This demonstrates writing a basic test function

from headline_module import Headline

def test_headline_creation():
    """
    Test that Headline objects are created correctly with the right attributes.
    This is the basic test for Step 2.
    """
    # Create a Headline instance with test data
    headline = Headline("General election: Labour and Tories clash over tax", "BBC News")
    
    # Assert that attributes are set correctly
    assert headline.text == "General election: Labour and Tories clash over tax"
    assert headline.source == "BBC News"
    
    print("✅ Basic test for object creation completed successfully!")

# Demonstrate the test (this would normally be run by pytest)
if __name__ == "__main__":
    print("Step 2: Basic Test for Object Creation")
    print("=" * 50)
    print("This demonstrates a basic test function.")
    print("In a real test file, pytest would run this automatically.")
    print("=" * 50)
    
    try:
        test_headline_creation()
        print("✅ Test passed! Headline object creation works correctly.")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    print("=" * 50)
    print("Next step: Write a test for the get_word_count method.")
