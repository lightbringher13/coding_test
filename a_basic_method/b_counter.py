from collections import Counter

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruits_count = Counter(fruits)
print(fruits_count)

text = "hello world"
char_count = Counter(text)
print(char_count)

# --------------------------------------------------------

# most_common method use after Counter
fruits_common = fruits_count.most_common(1)
print(fruits_common)

# --------------------------------------------------------

# You can update the counts by
# adding another iterable or another Counter object:
counter1 = Counter({'a': 2, 'b': 1})
counter2 = Counter({'a': 1, 'b': 2, 'c': 3})

# Update counter1 with counter2 counts
counter1.update(counter2)
print(counter1)  # Counter({'a': 3, 'b': 3, 'c': 3})

# --------------------------------------------------------

counter1 = Counter({'a': 5, 'b': 3, 'c': 2})
counter2 = Counter({'a': 1, 'b': 2})

# Subtract counter2 from counter1
counter1.subtract(counter2)
print(counter1)  # Counter({'a': 4, 'c': 2, 'b': 1})

# --------------------------------------------------------

counter = Counter(a=2, b=1, c=0)
print(list(counter.elements()))
# Output: ['a', 'a', 'b']

# --------------------------------------------------------
# arithmetic "+"
counter1 = Counter({'a': 3, 'b': 2})
counter2 = Counter({'a': 1, 'b': 3, 'c': 2})

result = counter1 + counter2
print(result)  # Output: Counter({'a': 4, 'b': 5, 'c': 2})

# --------------------------------------------------------
# arithmetic "-"
counter1 = Counter({'a': 3, 'b': 2})
counter2 = Counter({'a': 1, 'b': 3, 'c': 2})

result = counter1 - counter2
print(result)  # Output: Counter({'a': 2})

# --------------------------------------------------------
# arithmetic "&"
counter1 = Counter({'a': 3, 'b': 5})
counter2 = Counter({'a': 1, 'b': 7, 'c': 4})

result = counter1 & counter2
print(result)  # Output: Counter({'a': 1, 'b': 5})

# --------------------------------------------------------
# arithmetic "|"
counter1 = Counter({'a': 3, 'b': 5})
counter2 = Counter({'a': 1, 'b': 7, 'c': 4})

result = counter1 | counter2
print(result)  # Output: Counter({'b': 7, 'a': 3, 'c': 4})
