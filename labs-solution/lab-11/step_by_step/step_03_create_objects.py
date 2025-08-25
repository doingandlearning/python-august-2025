# Lab 11: Step 3 - Create Objects from File Data
# This demonstrates creating Headline objects from CSV data

import csv
from headline_module import Headline

def main():
    """
    Main function demonstrating Step 3 object creation.
    """
    print("Step 3: Create Objects from File Data")
    print("=" * 60)
    
    # Step 1: Prepare empty list
    headlines = []
    
    # Step 2: Open and read the CSV file
    filename = "headlines.csv"
    
    try:
        print(f"Opening '{filename}' and processing data...")
        
        with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
            # Create a CSV reader object
            csv_reader = csv.reader(csv_file)
            
            # Skip the header row
            next(csv_reader)
            
            # Step 3: Create Headline objects from file data
            print("\nProcessing rows and creating Headline objects...")
            print("-" * 50)
            
            for row_num, row in enumerate(csv_reader, 1):
                # Extract text and source from the row
                text = row[0]
                source = row[1]
                
                # Create a new Headline object
                headline = Headline(text, source)
                
                # Add the object to our headlines list
                headlines.append(headline)
                
                # Show progress for first few rows
                if row_num <= 3:
                    print(f"Row {row_num}: Created Headline object")
                    print(f"  Text: '{headline.text}'")
                    print(f"  Source: '{headline.source}'")
                    print(f"  Word count: {headline.get_word_count()}")
                    print()
                elif row_num == 4:
                    print("...")
            
            print(f"✅ Successfully created {len(headlines)} Headline objects")
            
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return
    except Exception as e:
        print(f"❌ Error processing file: {e}")
        return
    
    # Verify the results
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    
    if headlines:
        print(f"✅ Headlines list contains {len(headlines)} objects")
        print(f"✅ First headline: '{headlines[0].text}'")
        print(f"✅ Last headline: '{headlines[-1].text}'")
        
        # Test that the objects work correctly
        print(f"\n✅ Testing object functionality:")
        test_headline = headlines[0]
        print(f"  - Text attribute: '{test_headline.text}'")
        print(f"  - Source attribute: '{test_headline.source}'")
        print(f"  - Word count method: {test_headline.get_word_count()}")
        
    else:
        print("❌ No headlines were created")
    
    print("\n" + "=" * 60)
    print("Step 3 Complete!")
    print("Headline objects successfully created from CSV data.")
    print("The headlines list is now ready for analysis!")
    print("=" * 60)

if __name__ == "__main__":
    main()
