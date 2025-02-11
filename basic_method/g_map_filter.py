# It transforms the data from
# the input iterable by applying the function to each element.
def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)

# Convert the iterator to a list to see the results.
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Multiple Iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # Output: [5, 7, 9]

# ----------------------------------------------------------------
# filter()
# It is used for selecting items from an iterable
# that meet a condition return True


def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

# If you want to filter out “falsy” values
# (like 0, False, None, or empty strings/lists)
values = [0, 1, False, 2, '', 3, None, 4, [], 5]
filtered_values = filter(None, values)
print(list(filtered_values))  # Output: [1, 2, 3, 4, 5]
