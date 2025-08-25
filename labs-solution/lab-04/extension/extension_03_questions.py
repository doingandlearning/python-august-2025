# Extension 3: Find headlines that are questions
# This demonstrates string end checking and conditional logic

# Sample headlines (including some questions for demonstration)
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
    "Classic Doctor Who episodes to be released in colour",
    "Will the weather improve this weekend?",
    "How can we solve the climate crisis?",
    "What's next for the economy?"
]

print("=" * 60)
print("EXTENSION 3: FINDING QUESTION HEADLINES")
print("=" * 60)

# Find headlines that end with question marks
question_headlines = []
for headline in headlines:
    if headline.endswith('?'):
        question_headlines.append(headline)

# Display results
if question_headlines:
    print(f"Found {len(question_headlines)} question headline(s):")
    print("-" * 40)
    for i in range(len(question_headlines)):
        headline = question_headlines[i]
        print(f"{i+1}. {headline}")
else:
    print("No question headlines found.")
    print("Note: You can add headlines ending with '?' to test this feature.")

# Show all headlines with their question status
print("\n" + "-" * 40)
print("ALL HEADLINES WITH QUESTION STATUS")
print("-" * 40)

for i in range(len(headlines)):
    headline = headlines[i]
    if headline.endswith('?'):
        status = "QUESTION"
    else:
        status = "Statement"
    
    print(f"{i+1:2}. [{status:8}] {headline}")

# Count different types of headlines
question_count = len(question_headlines)
statement_count = len(headlines) - question_count

print(f"\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Total headlines: {len(headlines)}")
print(f"Question headlines: {question_count}")
print(f"Statement headlines: {statement_count}")
print(f"Percentage questions: {(question_count/len(headlines)*100):.1f}%")

print("\n" + "=" * 60)
print("Extension 3 Complete!")
print("=" * 60)
