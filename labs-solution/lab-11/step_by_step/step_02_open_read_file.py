# Lab 11: Step 2 - Open and Read the File
# This demonstrates opening the CSV file and creating a reader object

import csv
from headline_module import Headline

def main():
    """
    Main function demonstrating Step 2 file operations.
    """
    print("Step 2: Open and Read the CSV File")
    print("=" * 60)
    
    # Step 1: Prepare empty list
    headlines = []
    
    # Step 2: Open and read the CSV file
    filename = "headlines.csv"
    
    try:
        print(f"Attempting to open '{filename}'...")
        
        # Use the with statement for safe file handling
        with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
            print("✅ File opened successfully")
            
            # Create a CSV reader object
            csv_reader = csv.reader(csv_file)
            print("✅ CSV reader object created")
            
            # Skip the header row (text, source)
            header = next(csv_reader)
            print(f"✅ Header row skipped: {header}")
            
            # Count rows and show first few for demonstration
            row_count = 0
            print("\nFirst few rows of data:")
            print("-" * 40)
            
            for row in csv_reader:
                row_count += 1
                if row_count <= 3:  # Show first 3 rows
                    print(f"Row {row_count}: {row}")
                elif row_count == 4:
                    print("...")
                    break
            
            print(f"\n✅ Total data rows found: {row_count}")
            
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        print("Make sure headlines.csv is in the same directory as this script.")
        return
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return
    
    print("\n" + "=" * 60)
    print("Step 2 Complete!")
    print("File opened, CSV reader created, and header skipped.")
    print("Next: Create Headline objects from the file data")
    print("=" * 60)

if __name__ == "__main__":
    main()
