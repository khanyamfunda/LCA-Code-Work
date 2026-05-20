# -----------------------------------------------
# 🔁 Advanced Python Exercise 04: Loops & Modules
# -----------------------------------------------

# 💡 In this exercise, you'll work with lists, loops, the `random` module, and modular code using custom Python files.

# -----------------------------------------------
# Question 1: Iterating with Index and Value
# -----------------------------------------------

# 📝 Task:
# - Create a list called `dishes` with at least 5 South African traditional dishes.
# - Use a `for` loop and `enumerate()` to print each dish in this format:
#   "Dish 1: Bunny Chow"

# 💡 Tip:
# Use `enumerate(dishes, start=1)` to get both the index and the dish name.


# -----------------------------------------------
# Question 2: Countdown with Timer
# -----------------------------------------------

# 📝 Task:
# - Use a `while` loop to count down from 10 to 1.
# - Print each number with a 1-second pause between each.

# 💡 Tip:
# Import the `time` module and use `time.sleep(1)` to pause for one second between prints.


# -----------------------------------------------
# Question 3: Printing Squares and Cubes in a Table
# -----------------------------------------------

# 📝 Task:
# - Use a `for` loop with `range(1, 11)` to print a table of numbers 1 to 10.
# - For each number, print its square and cube neatly formatted in columns.

# 💡 Tip:
# Use formatted strings (f-strings) and alignment tricks like `:^6` for clean table layout.


# -----------------------------------------------
# Question 4: Random Selection with No Repeats
# -----------------------------------------------

# 📝 Task:
# - Create a list of 10 colours (e.g., red, blue, green, etc.).
# - Use `random.sample()` to select and print 5 unique colours without repetition.

# 💡 Tip:
# Import the `random` module and use `random.sample(list, 5)` to avoid duplicates.


# -----------------------------------------------
# Question 5: Using a Custom Module and Looping Calculator
# -----------------------------------------------

# 📝 Task:
# - Create a separate Python file named `math_advanced.py` containing four functions:
#   `add`, `subtract`, `multiply`, and `divide`.
# - In your main file, import that module and build a loop that:
#     - Takes two numbers and an operation from the user.
#     - Calls the corresponding function from the module.
#     - Repeats until the user types `q` to quit.

# 💡 Tip:
# Handle invalid operations and division by zero using if-else and try-except blocks.
# Create the file `math_advanced.py` with function definitions like:

# def add(a, b): return a + b
# def subtract(a, b): return a - b
# def multiply(a, b): return a * b
# def divide(a, b): return a / b if b != 0 else "Cannot divide by 0"

