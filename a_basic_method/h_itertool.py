import itertools

# cartesian product
# itertools.product(*iterables, repeat=1)
# repeat: How many times to repeat the product (defaults to 1).
a = [1, 2]
b = ['a', 'b']
result = list(itertools.product(a, b))
print("Product of [1, 2] and ['a', 'b']:", result)
# Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# using repeat
a = [1, 2]
result = list(itertools.product(a, repeat=3))
print("Product of [1, 2] repeated 3 times:", result)
# Output: [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2),
#          (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

# -------------------------------------------------------------------
# permutation(순열)
# itertools.permutations(iterable, r=None)
# Order matters here, and by default,
# it produces permutations of all elements.
a = [1, 2, 3]
result = list(itertools.permutations(a))
print("All full-length permutations of [1,2,3]:", result)
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3),
#          (2, 3, 1), (3, 1, 2), (3, 2, 1)]

a = [1, 2, 3]
result = list(itertools.permutations(a, 2))
print("2-element permutations of [1,2,3]:", result)
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# -------------------------------------------------------------------
# combination(조합)
# itertools.combinations(iterable, r)
# without replacement and where the order does not matter.
a = [1, 2, 3, 4]
result = list(itertools.combinations(a, 2))
print("2-element combinations of [1,2,3,4]:", result)
# Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# with replacement
a = [1, 2, 3]
result = list(itertools.combinations_with_replacement(a, 2))
print("2-element combinations with replacement of [1,2,3]:", result)
# Output: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
