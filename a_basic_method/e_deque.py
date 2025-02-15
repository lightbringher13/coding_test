from collections import deque
d = deque()
d = deque([1, 2, 3])
# d is now: deque([1, 2, 3])

# basic operations
# Appending to the Right:
d = deque()
d.append('a')
d.append('b')
print(d)  # deque(['a', 'b'])

# Appending to the Left:
d.appendleft('z')
print(d)  # deque(['z', 'a', 'b'])

# Popping from the Right:
right_item = d.pop()
print(right_item)  # 'b'
print(d)           # deque(['z', 'a'])

# Popping from the Left:
left_item = d.popleft()
print(left_item)  # 'z'
print(d)          # deque(['a'])

# Extending the Deque:
d.extend([40, 50])
print(d)  # deque([10, 20, 30, 40, 50])

d.extendleft([1, 2])
# The leftmost items are added in reverse order,
# so: deque([2, 1, 10, 20, 30, 40, 50])
print(d)

# Rotating:
# Positive value (e.g. rotate(1)): Rotates the deque to the right
# (the last element moves to the front)
# Negative value (e.g. rotate(-1)): Rotates the deque to the left
# (the first element moves to the back).
d = deque([1, 2, 3, 4, 5])
d.rotate(2)
print(d)  # deque([4, 5, 1, 2, 3])

d.rotate(-1)
print(d)  # deque([5, 1, 2, 3, 4])
