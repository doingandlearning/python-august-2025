Most learners hit a plateau after an introductory course—not because Python gets harder, but because the **next steps feel fuzzy**. Below is a curated map of resources, challenges and project ideas that work for _both_ non-developers and seasoned coders, and that play nicely with the BBC’s in-house O’Reilly subscription. Follow the sections in roughly the order given, mixing structured study with bite-size practice and small “automation wins” to keep momentum high.

---

## Structured Learning & Reference

### Real Python – “deep-dive articles + videos”

Free tutorials and paid learning paths cover everything from f-strings to async I/O, with quizzes to check retention ([realpython.com][1])

### Python Morsels – “one exercise per week”

Weekly graded challenges (novice → advanced) plus screencasts; ideal for habit building without overwhelm ([pythonmorsels.com][2])

### O’Reilly Learning Platform

Use the corporate subscription to stream **interactive** Python labs and classic books such as _Learning Python_ and _Fluent Python_; the platform’s “Interactive Learning” area lets you run code in-browser ([slo.oregon.gov][3], [en.wikipedia.org][4])

### Recommended Books

| Goal               | Title (O’Reilly or CC-licence)                        | Why it helps                                                     |
| ------------------ | ----------------------------------------------------- | ---------------------------------------------------------------- |
| Solid fundamentals | _Learning Python_ (Mark Lutz)                         | Deep coverage of core language ([cfm.ehu.es][5])                 |
| Practical wins     | _Automate the Boring Stuff with Python_ (Al Sweigart) | Project-based automation ideas ([automatetheboringstuff.com][6]) |

_(All are included in O’Reilly; Al Sweigart’s book is also free online.)_

---

## Practice & Daily Challenges

| Format                      | Platform                                                                                                                             | Why try it?                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| “25-day December puzzle”    | **Advent of Code**                                                                                                                   | Fresh problem each day; great pair-programming fodder ([adventofcode.com][7]) |
| Guided TDD drills           | **Exercism Python track** – 140+ exercises with mentor feedback ([exercism.org][8])                                                  |                                                                               |
| Real-world bite-sized katas | **PyBites / CodeChallenge.es** – emphasises idiomatic code ([codechalleng.es][9])                                                    |                                                                               |
| Data-centric notebooks      | **Kaggle Learn “Python” micro-courses** – interactive, no setup needed ([kaggle.com][10])                                            |                                                                               |
| Long-form habit builder     | **100 Days of Python** (Replit/Udemy/TalkPython variants) – build something daily for \~3 months ([replit.com][11], [udemy.com][12]) |                                                                               |
| Interview-style puzzles     | LeetCode / Codewars for those eyeing developer roles ([amazon.com][13])                                                              |                                                                               |

Mix one “evergreen” track (e.g. Exercism) with a seasonal burst (Advent of Code) to keep practice varied.

---

## Projects & Applied Learning

1. **Personal Automation** – re-implement _Automate the Boring Stuff_ scripts with your own BBC-adjacent tasks: bulk-rename files, scrape schedules, auto-format subtitles ([automatetheboringstuff.com][6])
2. **Data Snack-Size Projects**

   - Trending-topic dashboard using the headline toolkit from class.
   - Simple ETL: pull open data CSV → clean with pandas → push to SQLite.

3. **API Mash-ups** – build a CLI or Streamlit mini-app that hits the News API or the BBC Developer Portal for programme metadata.
4. **Kaggle Mini-Comp** – choose a beginner competition (Titanic, House Prices) to practise pandas, plotting and model baselines ([kaggle.com][10])
5. **“One-Module” Libraries** – publish a tiny package (e.g. `bbc-titlecase`) to PyPI; great real-world exposure to packaging and testing.

---

## Community & Support

| Community                   | Value                                                                            |
| --------------------------- | -------------------------------------------------------------------------------- |
| **Python Discord**          | Live help channels, monthly code jams ([en.wikipedia.org][14])                   |
| **r/learnpython** on Reddit | Peer Q\&A, book/course reviews ([reddit.com][15])                                |
| Real Python & PyBites Slack | Topic-specific chat and office-hours ([realpython.com][1], [codechalleng.es][9]) |
| O’Reilly live events        | Author Q\&A, “Superstream” one-day conferences ([slo.oregon.gov][3])             |

Joining one or two communities ensures you have humans in the loop when docs aren’t enough.

---

## Suggested Path (Developers vs Non-Developers)

| Profile                  | Next 4 Weeks                                               | After 4 Weeks                                                  |
| ------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------- |
| **Data-curious non-dev** | Real Python “Beginner Data” path + Automate chapters 1–6   | Kaggle Learn ➜ first mini project                              |
| **Junior dev**           | Python Morsels weekly + Exercism                           | Advent of Code or PyBites kata streak                          |
| **Experienced dev**      | O’Reilly _Fluent Python_ chapters + PyBites advanced track | Contribute mentor notes on Exercism; release a small PyPI tool |

---

### Final Tip

Treat learning as **cycling gears**: alternate focused reading (low gear) with real-world friction (high gear). These resources give you the gears—schedule the ride.

[1]: https://realpython.com/?utm_source=chatgpt.com "Real Python"
[2]: https://www.pythonmorsels.com/exercises/?utm_source=chatgpt.com "Python Exercises"
[3]: https://slo.oregon.gov/oreilly/content?utm_source=chatgpt.com "Content & Formats - O'Reilly Learning Platform"
[4]: https://en.wikipedia.org/wiki/O%27Reilly_Media?utm_source=chatgpt.com "O'Reilly Media"
[5]: https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf?utm_source=chatgpt.com "[PDF] Learning Python - Materials Physics Center"
[6]: https://automatetheboringstuff.com/?utm_source=chatgpt.com "Automate the Boring Stuff with Python"
[7]: https://adventofcode.com/?utm_source=chatgpt.com "Advent of Code 2024"
[8]: https://exercism.org/tracks/python?utm_source=chatgpt.com "Python on Exercism"
[9]: https://codechalleng.es/?utm_source=chatgpt.com "PyBites Platform | Real World Python Exercises"
[10]: https://www.kaggle.com/learn/python?utm_source=chatgpt.com "Learn Python Tutorials - Kaggle"
[11]: https://replit.com/learn/100-days-of-python/?utm_source=chatgpt.com "100 Days of Code - The Complete Python Course - Replit"
[12]: https://www.udemy.com/course/100-days-of-code/?srsltid=AfmBOoqlF3zmUQrcV5JTTUJSaUAK3X0SOHiek3QmtZ6JfM6D3CI6Uyq-&utm_source=chatgpt.com "100 Days of Code: The Complete Python Pro Bootcamp - Udemy"
[13]: https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994?utm_source=chatgpt.com "Automate the Boring Stuff with Python: Practical Programming for ..."
[14]: https://en.wikipedia.org/wiki/Advent_of_Code?utm_source=chatgpt.com "Advent of Code"
[15]: https://www.reddit.com/r/learnpython/comments/2jqgjw/is_it_possible_to_learn_python_by_reading_oreilly/?utm_source=chatgpt.com "Is it possible to learn Python by reading O'Reilly Learning ... - Reddit"
