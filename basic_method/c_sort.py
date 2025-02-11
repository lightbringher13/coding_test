# list Example using .sort()
numbers = [3, 1, 4, 1, 5, 9]
print("Original list:", numbers)

# Sort the list in ascending order in place.
numbers.sort()
print("After .sort():", numbers)

numbers = [3, 1, 4, 1, 5, 9]
# Sort in descending order by negating each element.
numbers.sort(key=lambda x: -x)
print("Sorted in descending order using key:", numbers)

# ---------------------------------------------------------
# dict example using sorted()
d = {"banana": 2, "apple": 3, "orange": 1}
sorted_keys = sorted(d)  # deafault using keys
print("Sorted keys:", sorted_keys)
# Output: Sorted keys: ['apple', 'banana', 'orange']

# return all the items
# if same follow the original order
sorted_items = sorted(d.items(), key=lambda item: item[1])
print("Items sorted by value:", sorted_items)
# Output: Items sorted by value: [('orange', 1), ('banana', 2), ('apple', 3)]

# Sort first by value, then by key in case of ties:
sorted_items = sorted(d.items(), key=lambda item: (item[1], item[0]))
print("Items sorted by value, then key:", sorted_items)
# Output: Items sorted by value, then key: [('orange', 1), ('apple', 3), ('banana', 2)]
