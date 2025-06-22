"""
Solution for the Final Case Study: Generating a News Source Report.
"""

import requests
from headline_module import Headline

# --- CONFIGURATION ---
# IMPORTANT: Replace "YOUR_API_KEY" with the key you get from newsapi.org
API_KEY = "9ec9a0b6703b490a86e6715f90185450"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


def load_headlines_from_api():
    """
    Loads headlines from the NewsAPI by specifying particular sources.
    
    Returns:
        A list of Headline objects, or an empty list if an error occurs.
    """
    params = {
        # On the free developer plan, we cannot filter by country or category.
        # Instead, we must specify one or more valid sources.
        'sources': 'bbc-news,independent',
        'apiKey': API_KEY
    }
    headlines = []
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        api_data = response.json()
        # The list of articles is under the 'articles' key
        articles = api_data.get("articles", [])

        for article_data in articles:
            # The source name is in a nested dictionary
            title = article_data.get("title", "No Title")
            source_dict = article_data.get("source", {})
            source = source_dict.get("name", "No Source")
            headlines.append(Headline(title, source))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except KeyError as e:
        print(f"Error parsing the API response: missing key {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return headlines


def analyze_sources(list_of_headlines):
    """
    Counts headlines per source and returns a dictionary.
    """
    source_counts = {}
    for headline in list_of_headlines:
        if headline.source in source_counts:
            source_counts[headline.source] += 1
        else:
            source_counts[headline.source] = 1
    return source_counts


def generate_report(analysis, total_headlines):
    """
    Generates a formatted report string from the analysis.
    """
    report_lines = [
        "--- NEWS SOURCE REPORT ---",
        f"There are {total_headlines} total headlines.",
        "The following sources were found:",
        ""  # Blank line for spacing
    ]

    # Sort the dictionary by value (count) in descending order
    sorted_analysis = sorted(analysis.items(), key=lambda item: item[1], reverse=True)

    for source, count in sorted_analysis:
        report_lines.append(f"* {source}: {count} headlines")

    return "\n".join(report_lines)


def main():
    """
    Main function to run the news analysis.
    """
    if API_KEY == "YOUR_API_KEY":
        print("Please replace 'YOUR_API_KEY' with your actual NewsAPI key.")
        return

    print("Loading headlines from the API...")
    headlines = load_headlines_from_api()

    if not headlines:
        print("No headlines loaded. Exiting.")
        return

    print(f"Loaded {len(headlines)} headlines.")

    # 2. Analyze the data
    analysis = analyze_sources(headlines)

    # 3. Generate the report string
    report = generate_report(analysis, len(headlines))

    # 4. Write the report to a file
    try:
        with open("report.txt", "w", encoding='utf-8') as f:
            f.write(report)
        print("Report generated successfully as report.txt")
    except IOError as e:
        print(f"Error writing report to file: {e}")


if __name__ == "__main__":
    main() 