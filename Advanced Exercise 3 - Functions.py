# -------------------------------------------
# Advanced Python Exercise 03: Functions
# -------------------------------------------

# Question 1: Function with Parameters and Conditional Logic
# TODO: Define a function `greet_user` that takes `name` and `role` as parameters.
#       If role is "admin", greet them with "Welcome Admin <name>!"
#       Otherwise, greet them with "Hello <name>, enjoy your session."

# TIP: Use an if-else statement inside the function.

# ------------------------------------------------------------------------------------

# Question 2: Function with Default and Keyword Arguments
# TODO: Define a function `register_student` with parameters:
#       `name`, `course`, and `country='South Africa'`.
#       It should print a formatted registration message using all the data.

# TODO: Call this function twice:
#       - Once using positional arguments
#       - Once using keyword arguments in a different order

# ------------------------------------------------------------------------------------

# Question 3: Returning Multiple Values
# TODO: Define a function `calculate_scores` that accepts 3 scores (int),
#       and returns the total and average.

# TODO: Unpack the returned values and print them separately

# TIP: Use the `return` keyword with comma-separated values.

# ------------------------------------------------------------------------------------

# Question 4: Nested Functions
# TODO: Define a function `student_progress` that:
#       - Accepts student name and 3 test scores
#       - Inside it, define another function `average_score` that calculates the average
#       - Return a message: "<name>'s average score is: <average>"

# ------------------------------------------------------------------------------------

# Question 5: Function as Arguments with Lambdas
# TODO: Define a function `apply_to_list` that takes a list and a function,
#       and applies the function to each item in the list using a loop.

# TODO: Use `apply_to_list` to double all items in `[1, 2, 3, 4]` using a lambda function.

# TODO: Then use it again to square all items in the same list using another lambda.

# TIP: Lambda functions are useful for short, anonymous operations.

# ------------------------------------------------------------------------------------

# Question 6: Optional Challenge - Flexible Arguments
# TODO: Create a function `describe_user` that accepts name, and any number of hobbies using `*args`.
#       It should print the name and list of hobbies in a friendly format.

# TODO: Call the function with 3 or more hobbies.

# TIP: Use a loop to iterate over `*args`.

