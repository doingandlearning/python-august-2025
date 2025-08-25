# Lab 10: Testing Demonstration Script
# This script demonstrates various testing concepts and pytest features

from headline_module import Headline

def demonstrate_testing_concepts():
    """
    Demonstrate various testing concepts without using pytest.
    """
    print("Lab 10: Testing Concepts Demonstration")
    print("=" * 60)
    
    # Test data
    test_cases = [
        ("Breaking news", "BBC News", 2),
        ("", "BBC News", 0),
        ("Single", "BBC News", 1),
        ("This is a longer headline with more words", "BBC News", 9),
        ("Climate change: Global impact", "BBC News", 4)
    ]
    
    print("Testing Headline class with various inputs:")
    print("-" * 40)
    
    passed_tests = 0
    total_tests = len(test_cases)
    
    for i, (text, source, expected_words) in enumerate(test_cases, 1):
        print(f"\nTest {i}: '{text}'")
        
        try:
            # Create headline object
            headline = Headline(text, source)
            
            # Test object creation
            assert headline.text == text, f"Text attribute mismatch: expected '{text}', got '{headline.text}'"
            assert headline.source == source, f"Source attribute mismatch: expected '{source}', got '{headline.source}'"
            
            # Test word count method
            actual_words = headline.get_word_count()
            assert actual_words == expected_words, f"Word count mismatch: expected {expected_words}, got {actual_words}"
            
            print(f"  ✅ PASSED: All assertions passed")
            passed_tests += 1
            
        except AssertionError as e:
            print(f"  ❌ FAILED: {e}")
        except Exception as e:
            print(f"  ❌ ERROR: Unexpected error - {e}")
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! The Headline class is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the implementation.")
    
    return passed_tests == total_tests

def demonstrate_edge_cases():
    """
    Demonstrate testing edge cases and boundary conditions.
    """
    print("\n" + "=" * 60)
    print("Testing Edge Cases and Boundary Conditions")
    print("=" * 60)
    
    edge_cases = [
        ("", "Empty string"),
        (" ", "Single space"),
        ("   ", "Multiple spaces"),
        ("a", "Single character"),
        ("123", "Numbers only"),
        ("!@#$%", "Special characters only"),
        ("a b c", "Single letters with spaces"),
        ("word1 word2 word3", "Words with numbers"),
        ("UPPERCASE WORDS", "All uppercase"),
        ("lowercase words", "All lowercase"),
        ("Mixed Case Words", "Mixed case"),
        ("word-with-hyphens", "Hyphenated words"),
        ("word.with.dots", "Words with dots"),
        ("word,with,commas", "Words with commas")
    ]
    
    print("Testing various edge cases:")
    print("-" * 40)
    
    for text, description in edge_cases:
        try:
            headline = Headline(text, "Test Source")
            word_count = headline.get_word_count()
            print(f"'{text}' ({description}): {word_count} words")
        except Exception as e:
            print(f"'{text}' ({description}): ERROR - {e}")

def demonstrate_test_organization():
    """
    Demonstrate how tests can be organized and structured.
    """
    print("\n" + "=" * 60)
    print("Test Organization and Structure")
    print("=" * 60)
    
    print("1. Test Function Naming:")
    print("   - test_headline_creation()")
    print("   - test_get_word_count()")
    print("   - test_edge_cases()")
    print("   - test_fixtures()")
    
    print("\n2. Test Categories:")
    print("   - Object creation tests")
    print("   - Method functionality tests")
    print("   - Edge case tests")
    print("   - Integration tests")
    
    print("\n3. Test Data Organization:")
    print("   - Simple test cases")
    print("   - Edge cases")
    print("   - Boundary conditions")
    print("   - Error conditions")
    
    print("\n4. Assertion Types:")
    print("   - Equality assertions (==)")
    print("   - Inequality assertions (!=)")
    print("   - Boolean assertions (True/False)")
    print("   - Exception assertions (raises)")

def demonstrate_pytest_commands():
    """
    Show common pytest commands and their usage.
    """
    print("\n" + "=" * 60)
    print("Pytest Commands and Usage")
    print("=" * 60)
    
    commands = [
        ("pytest", "Run all tests in current directory"),
        ("pytest -v", "Verbose output showing each test"),
        ("pytest -k 'test_name'", "Run tests matching pattern"),
        ("pytest test_file.py", "Run tests in specific file"),
        ("pytest --tb=short", "Shorter traceback for failures"),
        ("pytest --tb=no", "No traceback for failures"),
        ("pytest -x", "Stop after first failure"),
        ("pytest --maxfail=3", "Stop after 3 failures"),
        ("pytest --collect-only", "Show what tests would run"),
        ("pytest --version", "Show pytest version")
    ]
    
    for command, description in commands:
        print(f"  {command:<25} - {description}")

if __name__ == "__main__":
    # Run all demonstrations
    demonstrate_testing_concepts()
    demonstrate_edge_cases()
    demonstrate_test_organization()
    demonstrate_pytest_commands()
    
    print("\n" + "=" * 60)
    print("Testing Demonstration Complete!")
    print("=" * 60)
    print("Key Takeaways:")
    print("- Tests verify your code works correctly")
    print("- Edge cases are important to test")
    print("- Good test organization makes maintenance easier")
    print("- pytest provides powerful testing tools")
    print("- Automated testing saves time and prevents bugs")
    print("=" * 60)
