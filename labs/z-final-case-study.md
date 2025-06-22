# Lab Z: Final Case Study - Live News Analysis

In this final case-study, you will bring together all the skills you have learned in this course to build a complete news analysis application.

You'll be reading live news data from the internet, processing it using a class you design, performing analysis, and writing a report to a file.

## The Goal

Your task is to fetch recent news headlines from a live API, analyze the sources of these headlines, and generate a `report.txt` file that summarizes how many headlines came from each source.

The final output, `report.txt`, should look something like this:

```text
--- NEWS SOURCE REPORT ---
There are 40 total headlines.
The following sources were found:

* BBC News: 10 headlines
* Reuters: 8 headlines
* The Guardian: 7 headlines
* ...and so on for all sources
```

## Core Concepts Review

This lab will require you to use:

*   **File I/O:** To write your final report.
*   **APIs & Networking:** To fetch the live headline data.
*   **Lists & Dictionaries:** To store and analyze the data.
*   **Classes:** To structure your headline data neatly.
*   **Functions:** To organize your code into logical, reusable blocks.
*   **Modules:** To keep your code clean and separated.

---

## Setup: API Key and 'requests' library

### 1. Install the 'requests' library

To fetch data from the internet, we need a library to handle the HTTP requests for us. The most popular one in Python is called `requests`. If you haven't already, open your terminal or command prompt and run the following command:

```bash
pip install requests
```

### 2. Get a NewsAPI Key

The API we will be using is [NewsAPI](https://newsapi.org/), a professional and widely-used service. It requires an API key to identify your requests.

For this course, a key will be provided to you. In a real-world project, you would go to their website and register for a free developer key.

---

## Step 1: The `headline_module.py`

This step is the same as the one from the Modules and Testing labs.

Create a file named `headline_module.py`. In this file, define the `Headline` class.

**`Headline` Class Requirements:**

*   An `__init__` method that accepts `title` and `source` as arguments and stores them as attributes.
*   A `__str__` method that returns a formatted string, for example: `"The title is 'The Title' from 'The Source'"`

> **Hint:** You can copy the class you created in the Classes lab.

## Step 2: The `main_analysis.py`

Create a second file named `main_analysis.py`. This will be where the main logic of your application lives.

Start by importing the `Headline` class from your `headline_module.py` and the `requests` library.

```python
import requests
from headline_module import Headline
```

## Step 3: Fetching the Data from the API

We will fetch live data from **NewsAPI**. The endpoint we will use is `https://newsapi.org/v2/top-headlines`.

A key limitation of the free "Developer" plan on NewsAPI is that you cannot filter by `country` or `category`. You can only fetch headlines from a specific list of `sources`. This is a common practice for APIs to encourage users to move to paid plans for more advanced filtering.

For our lab, we will request headlines from a few major english-speaking sources like the BBC and Independent.

The data comes back in a format called **JSON**. It will look something like this:

```json
{
  "status": "ok",
  "totalResults": 38,
  "articles": [
    {
      "source": { "id": "bBC-news", "name": "BBC News" },
      "author": "BBC News",
      "title": "UK economy grows more slowly than expected in January - BBC News",
      "description": "The economy grew by 0.8% at the start of the year, but is still smaller than before the pandemic.",
      "url": "https://www.bbc.co.uk/news/business-60706216",
      "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/1547F/production/_123633538_mediaitem123633537.jpg",
      "publishedAt": "2022-03-11T07:49:35Z",
      "content": "By Faisal Islam, economics editor"
    },
    {
       "source": { "id": "reuters", "name": "Reuters" },
       "author": null,
       "title": "ECB to stop bond-buying,..."
       /* ... more fields ... */
    }
  ]
}
```

Notice two important things:
1.  The actual news articles are in a list under the `articles` key.
2.  The source's name is nested inside a dictionary under the `source` key.

**Your Task:**

Create a function `load_headlines_from_api(api_key)` that does the following:

1.  Accepts your `api_key` as an argument.
2.  Defines the URL: `https://newsapi.org/v2/top-headlines`.
3.  Defines the parameters for the request. Create a dictionary `params` that includes the `sources` (e.g., `'bbc-news,independent'`) and your `apiKey`.
4.  Sends the request using `requests.get(url, params=params)`.
5.  Add robust error handling with a `try...except` block and check `response.status_code`.
6.  If successful, get the JSON data. Access the list of articles using `response.json()['articles']`.
7.  Create an empty list for your `Headline` objects.
8.  Loop through the list of article dictionaries. In each iteration:
    *   Extract the `title`.
    *   Extract the source's `name` from the nested `source` dictionary. Be careful! Use `.get()` to avoid errors if a key is missing. e.g., `article_data.get('source', {}).get('name')`.
    *   Create a `Headline` object.
    *   Append it to your list.
9.  Return the list of `Headline` objects.

## Step 4: Analyzing the Sources

Create a function `analyze_sources(headlines)` that takes the list of `Headline` objects and returns a dictionary.

*   The **keys** of the dictionary should be the news sources (e.g., `'belfasttelegraph.co.uk'`).
*   The **values** should be the number of times that source appeared.

**Example output:** `{'belfasttelegraph.co.uk': 10, 'hindustantimes.com': 8}`

> **Hint:** You can loop through the list of `Headline` objects. For each object, check if its `source` is already a key in your results dictionary. If it is, increment the value. If not, add it to the dictionary with a value of 1.

## Step 5: Generating the Report

Create a function `generate_report(analysis, total_headlines)` that takes the source analysis dictionary and the total number of headlines.

This function should create a multi-line string containing the formatted report, as shown in the "Goal" section at the top.

> **Hint:** Start with a header string. Then, loop through the `analysis` dictionary's items (`.items()`) to build the list of sources and their counts.

## Step 6: Putting It All Together

Create a `main()` function and use the `if __name__ == "__main__":` block to call it.

The `main()` function should:

1.  **Store your API key.** Create a variable at the top of your script (or inside main) and assign your API key string to it. **Do not share this key publicly.**
2.  Call `load_headlines_from_api()` with your key to get the headlines.
3.  Check if any headlines were returned. If not, print a message and exit.
4.  Call `analyze_sources()` to get the source analysis.
5.  Call `generate_report()` to create the report string.
6.  Open `report.txt` in write mode (`'w'`) and save the report. Remember to specify `encoding='utf-8'` to handle special characters.
7.  Print a confirmation message to the console.

---

Good luck! This final lab is your chance to see how all the individual pieces you've learned can come together to create a useful, real-world application. 