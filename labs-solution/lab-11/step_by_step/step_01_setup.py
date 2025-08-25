# Lab 11: Step 1 - Getting Started
# This demonstrates the basic setup for reading from CSV files

# Step 1: Import the csv module
import csv

# Import the Headline class from our module
from headline_module import Headline

def main():
    """
    Main function demonstrating Step 1 setup.
    """
    print("Step 1: Getting Started with File Reading")
    print("=" * 60)
    
    # Step 1: Prepare an empty list for headlines
    headlines = []
    
    print("✅ CSV module imported successfully")
    print("✅ Headline class imported successfully")
    print("✅ Empty headlines list created")
    print(f"✅ Headlines list length: {len(headlines)}")
    
    # Verify we can create Headline objects (basic functionality check)
    try:
        test_headline = Headline("Test headline", "Test Source")
        print("✅ Headline object creation test passed")
        print(f"   Test headline text: '{test_headline.text}'")
        print(f"   Test headline source: '{test_headline.source}'")
        
    except Exception as e:
        print(f"❌ Error creating test headline: {e}")
        print("Make sure headline_module.py is in the same directory.")
    
    print("\n" + "=" * 60)
    print("Step 1 Complete!")
    print("Next: Open and read the CSV file")
    print("=" * 60)

if __name__ == "__main__":
    main()
