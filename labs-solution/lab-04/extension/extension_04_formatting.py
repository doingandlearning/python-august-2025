# Extension 4: Uniform capitalization
# This demonstrates the .title() method and text formatting

# Sample headlines
headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Debate rages over future of Artificial Intelligence",
    "Classic Doctor Who episodes to be released in colour"
]

print("=" * 60)
print("EXTENSION 4: UNIFORM FORMATTING")
print("=" * 60)

# Show original headlines
print("ORIGINAL HEADLINES:")
print("-" * 40)
for i in range(len(headlines)):
    headline = headlines[i]
    print(f"{i+1:2}. {headline}")

# Apply title case formatting
print("\n" + "-" * 40)
print("TITLE CASE FORMATTING:")
print("-" * 40)
for i in range(len(headlines)):
    headline = headlines[i]
    title_case = headline.title()
    print(f"{i+1:2}. {title_case}")

# Show comparison side by side
print("\n" + "=" * 60)
print("SIDE-BY-SIDE COMPARISON")
print("=" * 60)

for i in range(len(headlines)):
    original = headlines[i]
    formatted = original.title()
    
    print(f"{i+1:2}. Original:  {original}")
    print(f"   Formatted: {formatted}")
    print()

# Check for potential formatting issues
print("=" * 60)
print("FORMATTING ANALYSIS")
print("=" * 60)

print("Potential issues with title case:")
print("- Acronyms like 'NHS' become 'Nhs'")
print("- Numbers remain unchanged")
print("- Punctuation is preserved")
print("- All words get first letter capitalized")

# Show specific examples of formatting changes
print("\nSpecific examples:")
for i in range(min(5, len(headlines))):
    original = headlines[i]
    formatted = original.title()
    
    if original != formatted:
        print(f"'{original}' -> '{formatted}'")
    else:
        print(f"'{original}' (no change)")

print("\n" + "=" * 60)
print("Extension 4 Complete!")
print("=" * 60)
