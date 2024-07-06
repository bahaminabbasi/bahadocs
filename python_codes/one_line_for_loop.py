"""
A one-liner for loop in Python, also known as a list comprehension, 
allows you to create lists, dictionaries, or sets in a single line by specifying
an expression followed by a for clause.
"""

## FORMULA ##
# [expression for item in iterable]

## EXAMPLES ##
# 1 - List of squares of numbers from 1 to 10:
squares = [x**2 for x in range(1, 11)]
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

###############################################################################
# 2 - List of even numbers from 1 to 20:
evens = [x for x in range(1, 21) if x % 2 == 0]
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

###############################################################################
# 3 - Convert a list of strings to uppercase:
words = ["hello", "world", "python"]

upper_words = [word.upper() for word in words]
# Output: ['HELLO', 'WORLD', 'PYTHON']

###############################################################################
# 4 - Dictionary of numbers and their squares:
squares_dict = {x: x**2 for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

###############################################################################
# 5 - Set of unique characters in a string:
unique_chars = {char for char in "abracadabra"}
# Output: {'a', 'b', 'c', 'd', 'r'}

###############################################################################
# 6 - Flatten a list of lists:
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = [item for sublist in list_of_lists for item in sublist]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

###############################################################################
# 7 - Example from Robust Python page 6
recipe = [
    ('flour', 2, 'cups'),
    ('sugar', 1, 'cup'),
    ('eggs', 3, 'units'),
    ('milk', 1, 'cup')
]

factor = 2  # We want to double the recipe
new_recipe = {ingredient: (amount * factor, unit)
              for ingredient, amount, unit in recipe}
# Output {'flour': (4, 'cups'), 'sugar': (2, 'cup'), 'eggs': (6, 'units'), 'milk': (2, 'cup')}