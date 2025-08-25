# Lab 10: Step 1 - Setup
# This demonstrates the basic setup for testing with pytest

# Import the class we want to test
from headline_module import Headline

print("Step 1: Basic Setup for Testing")
print("=" * 50)
print("✅ Test file created: test_headline.py")
print("✅ pytest installed (run: pip install pytest)")
print("✅ Headline class imported successfully")
print("=" * 50)

# Verify we can create a Headline object (basic functionality check)
try:
    test_headline = Headline("Test headline", "Test Source")
    print(f"✅ Headline object created successfully:")
    print(f"   Text: '{test_headline.text}'")
    print(f"   Source: '{test_headline.source}'")
    print("=" * 50)
    print("Setup complete! Ready to write tests.")
    
except Exception as e:
    print(f"❌ Error during setup: {e}")
    print("Make sure headline_module.py is in the same directory.")
    print("=" * 50)
