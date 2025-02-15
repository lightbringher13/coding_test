# reversed() vs .reverse()
# .reversed() does not work with tuple, string immutable object
my_list = [1, 2, 3, 4]
for item in reversed(my_list):
    print(item)
# This prints: 4, 3, 2, 1 (each on a new line)

# reversed() returns an iterator, so
# if you need a list in reverse order
# you can wrap it with list():
reversed_list = list(reversed(my_list))
print(reversed_list)  # Output: [4, 3, 2, 1]
