# Lab 11: File Operations Demonstration Script
# This script demonstrates various file operations and CSV processing techniques

import csv
import os
from headline_module import Headline

def demonstrate_file_operations():
    """
    Demonstrate basic file operations and CSV processing.
    """
    print("Lab 11: File Operations Demonstration")
    print("=" * 70)
    
    # Check if headlines.csv exists
    filename = "headlines.csv"
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' not found. Creating a sample file...")
        create_sample_csv(filename)
    
    print(f"✅ Working with file: {filename}")
    print("=" * 70)
    
    # Demonstrate different file reading approaches
    print("\n1. BASIC FILE READING")
    print("-" * 40)
    basic_file_reading(filename)
    
    print("\n2. CSV PROCESSING")
    print("-" * 40)
    csv_processing_demo(filename)
    
    print("\n3. ERROR HANDLING")
    print("-" * 40)
    error_handling_demo()
    
    print("\n4. DATA VALIDATION")
    print("-" * 40)
    data_validation_demo(filename)
    
    print("\n5. FILE STATISTICS")
    print("-" * 40)
    file_statistics_demo(filename)

def create_sample_csv(filename):
    """
    Create a sample CSV file for demonstration purposes.
    """
    sample_data = [
        ["text", "source"],
        ["Breaking news: Major announcement today", "BBC News"],
        ["Technology advances in artificial intelligence", "Tech Daily"],
        ["Sports team wins championship", "Sports Central"],
        ["Weather forecast for the weekend", "Weather Channel"],
        ["New restaurant opens in downtown", "Local News"]
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sample_data)
    
    print(f"✅ Sample CSV file '{filename}' created successfully")

def basic_file_reading(filename):
    """
    Demonstrate basic file reading operations.
    """
    print("Reading file as plain text:")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            
            print(f"✅ File opened successfully")
            print(f"✅ Total lines: {len(lines)}")
            print(f"✅ File size: {len(content)} characters")
            
            print("\nFirst 3 lines:")
            for i, line in enumerate(lines[:3]):
                print(f"  {i+1}: {line}")
            
            if len(lines) > 3:
                print("  ...")
                
    except Exception as e:
        print(f"❌ Error reading file: {e}")

def csv_processing_demo(filename):
    """
    Demonstrate CSV processing techniques.
    """
    print("Processing CSV file with different approaches:")
    
    # Approach 1: Basic CSV reading
    print("\nApproach 1: Basic CSV reading")
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            
            print(f"✅ Total rows: {len(rows)}")
            print(f"✅ Header: {rows[0]}")
            print(f"✅ Data rows: {len(rows) - 1}")
            
            if len(rows) > 1:
                print(f"✅ First data row: {rows[1]}")
                
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Approach 2: Row by row processing
    print("\nApproach 2: Row by row processing")
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Skip header
            
            row_count = 0
            for row in reader:
                row_count += 1
                if row_count <= 2:  # Show first 2 data rows
                    print(f"  Row {row_count}: {row}")
            
            if row_count > 2:
                print("  ...")
            print(f"✅ Processed {row_count} data rows")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def error_handling_demo():
    """
    Demonstrate error handling for file operations.
    """
    print("Testing error handling scenarios:")
    
    # Test 1: File not found
    print("\nTest 1: File not found")
    try:
        with open("nonexistent_file.csv", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("✅ Correctly handled: File not found")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    # Test 2: Permission error (simulated)
    print("\nTest 2: Permission error (simulated)")
    try:
        # This would normally cause a permission error
        with open("/root/test.csv", 'r') as file:
            content = file.read()
    except PermissionError:
        print("✅ Correctly handled: Permission denied")
    except FileNotFoundError:
        print("✅ Correctly handled: File not found")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    # Test 3: CSV parsing error (simulated)
    print("\nTest 3: CSV parsing error (simulated)")
    try:
        # Create a malformed CSV string
        malformed_csv = "text,source\n'Unclosed quote,source\n"
        reader = csv.reader(malformed_csv.splitlines())
        rows = list(reader)
        print(f"✅ CSV parsed successfully: {len(rows)} rows")
    except Exception as e:
        print(f"✅ Correctly handled: CSV parsing error - {e}")

def data_validation_demo(filename):
    """
    Demonstrate data validation techniques.
    """
    print("Data validation examples:")
    
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            
            # Validate header
            print(f"\nHeader validation:")
            print(f"  Expected columns: ['text', 'source']")
            print(f"  Actual columns: {header}")
            
            if header == ['text', 'source']:
                print("  ✅ Header format is correct")
            else:
                print("  ❌ Header format is incorrect")
            
            # Validate data rows
            print(f"\nData validation:")
            row_count = 0
            valid_rows = 0
            empty_rows = 0
            
            for row in reader:
                row_count += 1
                
                # Check if row has expected number of columns
                if len(row) == 2:
                    valid_rows += 1
                    
                    # Check if text is not empty
                    if row[0].strip():
                        pass  # Text is valid
                    else:
                        print(f"  ⚠️  Row {row_count}: Empty text")
                else:
                    print(f"  ❌ Row {row_count}: Wrong number of columns ({len(row)})")
                
                # Check for empty rows
                if not any(cell.strip() for cell in row):
                    empty_rows += 1
            
            print(f"  ✅ Total rows processed: {row_count}")
            print(f"  ✅ Valid rows: {valid_rows}")
            print(f"  ⚠️  Empty rows: {empty_rows}")
            
    except Exception as e:
        print(f"❌ Error during validation: {e}")

def file_statistics_demo(filename):
    """
    Demonstrate file and data statistics.
    """
    print("File and data statistics:")
    
    try:
        # File statistics
        file_size = os.path.getsize(filename)
        print(f"\nFile statistics:")
        print(f"  File size: {file_size} bytes")
        print(f"  File size: {file_size / 1024:.2f} KB")
        
        # Data statistics
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            
            total_chars = 0
            total_words = 0
            row_count = 0
            
            for row in reader:
                row_count += 1
                if len(row) >= 1:
                    text = row[0]
                    total_chars += len(text)
                    total_words += len(text.split())
            
            print(f"\nData statistics:")
            print(f"  Total data rows: {row_count}")
            print(f"  Total characters: {total_chars}")
            print(f"  Total words: {total_words}")
            if row_count > 0:
                print(f"  Average characters per row: {total_chars / row_count:.1f}")
                print(f"  Average words per row: {total_words / row_count:.1f}")
        
    except Exception as e:
        print(f"❌ Error calculating statistics: {e}")

if __name__ == "__main__":
    demonstrate_file_operations()
    
    print("\n" + "=" * 70)
    print("File Operations Demonstration Complete!")
    print("=" * 70)
    print("Key Takeaways:")
    print("- Always use 'with' statements for file operations")
    print("- Handle errors gracefully with try-except blocks")
    print("- Validate data as you read it")
    print("- Use appropriate encoding for text files")
    print("- CSV files are just structured text files")
    print("- File I/O separates data from program logic")
    print("=" * 70)
