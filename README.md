# 🐍 PYTHON 

Welcome to this Python ! This repository contains Python code that demonstrates basic programming concepts and features of the Python language.

---

## 📖 What is Python?

**Python** is a high-level, interpreted programming language created by **Guido van Rossum** and released in **1991**. It emphasizes readability, simplicity, and flexibility, making it popular for both beginners and professionals.

Python supports multiple programming paradigms including object-oriented, procedural, and functional programming.

---

## 🚀 Features of Python

- Clean and readable syntax
- Interpreted (no need to compile)
- Dynamically typed
- Extensive standard library
- Cross-platform compatibility
- Large community and support
- Great for web development, data science, machine learning, scripting, and more

## 💡 What Can You Build With Python?

- Web applications (e.g. Django, Flask)
- Data analysis and visualization (e.g. Pandas, Matplotlib)
- Machine learning and AI (e.g. TensorFlow, scikit-learn)
- Scripting and automation
- Desktop applications
- Games and simulations
- Internet of Things (IoT) and robotics
- APIs and backend services

---

## 💻 Python Installation

To run Python code, you need to have Python installed on your system. Follow the steps below to install Python.

### ✅ Step 1: Download Python

Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Choose the appropriate installer for your operating system:

- **Windows**: Download the `.exe` installer
- **macOS**: Download the `.pkg` installer
- **Linux**: Use your system's package manager (see below)

---

### 🪟 Windows

1. Download the latest version from the [Python Downloads](https://www.python.org/downloads/windows/) page.
2. Run the installer.
3. **Important**: Check the box that says **"Add Python to PATH"**.
4. Click **Install Now**.

---


---

# 📘 Python Data Types: Strings, Lists, and Tuples

This document provides an overview of three core data types in Python: **Strings**, **Lists**, and **Tuples**.

---

## 🔤 Strings (`str`)

Strings are **immutable** sequences of characters used to represent text.

### ✅ Declaration
```python
name = "Alice"
greeting = 'Hello, world!'
multiline = """This is
a multiline string."""
```

## 📋 Lists (`list`)

Lists are **mutable**, ordered collections that can store multiple items, including different data types. Lists are one of the most commonly used data structures in Python.

---

### ✅ Declaration

You can create a list using square brackets `[]`:

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
empty = []

```
## 📦 Tuples (`tuple`)

Tuples are **immutable**, ordered collections in Python. They are used to store a fixed set of values that should not be changed during the execution of a program.

---

### ✅ Declaration

You can create a tuple using parentheses `()`:

```python
colors = ("red", "green", "blue")
numbers = (1, 2, 3, 4)
mixed = ("hello", 42, True, 3.14)

# Single-item tuple (note the trailing comma)
single = ("one",)

```

## 🔍 Differences at a Glance

| Feature   | String        | List | Tuple         |
| --------- | ------------- | ---- | ------------- |
| Ordered   | ✅             | ✅    | ✅             |
| Mutable   | ❌ (immutable) | ✅    | ❌ (immutable) |
| Indexable | ✅             | ✅    | ✅             |
| Iterable  | ✅             | ✅    | ✅             |

## 🗂️ DICTIONARY

A **dictionary** in Python is an unordered collection of key-value pairs. It is used to store data values where each value is accessed by a unique key.

## Syntax

```python
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

## Dictionary method 

| Method          | Description                                  |
| --------------- | -------------------------------------------- |
| `dict.get(key)` | Returns the value for the key if exists      |
| `dict.keys()`   | Returns a view object of all keys            |
| `dict.values()` | Returns a view object of all values          |
| `dict.items()`  | Returns a view object of all key-value pairs |
| `dict.pop(key)` | Removes and returns the value for the key    |
| `dict.clear()`  | Removes all items from the dictionary        |

## 🔁 SET

A **set** in Python is an unordered collection of **unique** and **immutable** elements. Sets are useful for membership testing, removing duplicates, and performing mathematical set operations like union, intersection, and difference.

## Syntax

```python
my_set = {1, 2, 3, 4}
```

## Set method 

| Method             | Description                                  |
| ------------------ | -------------------------------------------- |
| `add(x)`           | Adds element `x` to the set                  |
| `remove(x)`        | Removes element `x` (raises error if absent) |
| `discard(x)`       | Removes element `x` (no error if absent)     |
| `clear()`          | Removes all elements                         |
| `copy()`           | Returns a shallow copy                       |
| `pop()`            | Removes and returns a random element         |

## 🔁 Python `while` Loop

The `while` loop in Python is used to repeatedly execute a block of code **as long as a specified condition is `True`**.

### EXAMPLE
```
counter = 0

while counter < 5:
    print("Counter is:", counter)
    counter += 1
```
## 🔁 for Loop in Python

The `for` loop in Python is used to iterate over sequences such as lists, strings, tuples, or ranges.

### 🔹 Examples

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```











