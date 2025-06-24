## 🧩 Suggested Extensions for Lab 4: _Analyzing News Headlines_

### 🔁 List & String Processing Extensions

1. **Sort headlines by length**

   - Print the top 3 longest or shortest headlines.

2. **Count total characters**

   - Not just words — what’s the total number of characters across all headlines?

3. **Find headlines that are questions**

   - Look for `?` at the end.

4. **Capitalize all headlines uniformly**

   - Title case all headlines using `.title()`.

5. **Print all headlines containing numbers**

   - Use `any(char.isdigit() for char in headline)`.

---

### 🧠 Introduce Data Structures

6. **Create a dictionary of headline lengths**

   - `{"headline text": word_count}`
   - Preview for tomorrow’s dictionaries lesson.

7. **Group headlines by first word**

   - Create a dictionary where the key is the first word (`"General"`, `"Science"`, etc.), and the value is a list of matching headlines.

---

### 🧪 Logic and Searching

8. **Support multiple search terms**

   - Let the user enter `"NHS, AI, inflation"` and split on commas to support multiple topic searches.

9. **Highlight the search term in the headline**

   - Reprint the headline with the matched word in `ALL CAPS` or surrounded by `*asterisks*`.

---

### 🧮 Stretch Challenge

10. **Build a simple frequency counter**

    - Count how often each **word** appears across all headlines (hint: dictionary + `.split()`).
    - Print the top 5 most frequent words.
