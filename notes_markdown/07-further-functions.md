# Plan for Session
- Local & Global Variables
- Modifying Globals within a function
- Anonymous / Lambda Functions
- List Comprehensions - a powerful alternative to map and filter

---

## Local & Global Variables
- Variables can be declared as being global (to the program) or local to a function.
- Local variables can only be referenced within the scope they are defined in.
- Global variables can be referenced anywhere.

### Example:
```python
a_global_count = 10

def some_func():
    a_local_variable = 100
    print('a_local_variable:', a_local_variable)
    print('a_global_count:', a_global_count)

some_func()
```

---

## Modifying Globals within a Function
- By default, local variables will hide global variables with the same name (known as 'Shadowing').

### Example:
```python
def my_function():
    a_variable = 100
    print('inside function:', a_variable)

a_variable = 25

print('before function:', a_variable)
my_function()
print('outside function:', a_variable)
```

- To modify a global variable within a function, it must first be declared as `global` inside the function before use.

### Example:
```python
max = 100

print('initial value of max:', max)

def print_max():
    global max
    max = max + 1
    print('inside function:', max)

print_max()
print('outside function:', max)
```

---

## Anonymous / Lambda Functions
- Can define anonymous functions, also known as lambda functions.
- Can optionally take parameters.
- Always return a value.

### Syntax:
```python
lambda arguments: expression
```

### Example:
```python
func0 = lambda: print('no args')
func1 = lambda x: x * x
func2 = lambda x, y: x * y
func3 = lambda x, y, z: x + y + z

func0()
print(func1(4))
print(func2(3, 4))
print(func3(2, 3, 4))
```

---

## List Comprehensions: A Powerful Alternative

While Python offers functional programming tools like `map` and `filter`, a more common and often more readable approach is to use **list comprehensions**. They provide a concise way to create lists based on existing lists.

### Basic Syntax (Mapping)
You can use a list comprehension to apply an expression to every item in a list, similar to `map`.

**Syntax:** `[expression for item in list]`

**Example:** Let's get the word count for each headline.
```python
headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom"
]

word_counts = [len(h.split()) for h in headlines]
print(word_counts)
# Output: [7, 5, 7]
```

### Adding a Condition (Filtering)
You can add an `if` condition to the end of a list comprehension to filter items from the original list, similar to `filter`.

**Syntax:** `[item for item in list if condition]`

**Example:** Let's find only the headlines that mention "tax".
```python
headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom"
]

tax_headlines = [h for h in headlines if 'tax' in h.lower()]
print(tax_headlines)
# Output: ['General election: Labour and Tories clash over tax']
```

### Combining Mapping and Filtering
You can combine both to perform a mapping operation on a filtered set of data.

**Example:** Let's get the word counts of only the headlines that are longer than 6 words.
```python
headlines = [
    "General election: Labour and Tories clash over tax", # 7 words
    "England crowned T20 world champions", # 5 words
    "Summer travel chaos feared as airline strikes loom", # 7 words
    "New David Hockney exhibition opens in London" # 7 words
]

long_headline_lengths = [len(h.split()) for h in headlines if len(h.split()) > 6]
print(long_headline_lengths)
# Output: [7, 7, 7]
```
List comprehensions are a powerful and widely-used feature of Python for data manipulation.

---

## Questions?

?
