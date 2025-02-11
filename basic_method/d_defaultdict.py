from collections import defaultdict

# Create a defaultdict that provides a default value of 0 for missing keys.
counts = defaultdict(int)
print(counts["apple"])  # Since "apple" doesn't exist yet, int() returns 0.
counts["apple"] += 1
print(counts["apple"])  # Now it prints 1.


# Create a defaultdict where the default value for any new key is an empty list.
d = defaultdict(list)

# Access a key that hasn't been set yet.
print(d["new_key"])  # Output: []

# Now you can directly append to this empty list.
d["new_key"].append("value")
print(d["new_key"])  # Output: ['value']

# -----------------------------------------------------------------------
# examples of grouping
# Each missing key will have an empty list as its default value.
groups = defaultdict(list)
words = ["apple", "banana", "avocado", "blueberry", "cherry"]

for word in words:
    groups[word[0]].append(word)

print(groups)
# Example output: defaultdict(<class 'list'>, {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']})
