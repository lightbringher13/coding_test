from itertools import product


def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    words_list = []

    # Generate all possible words with lengths 1 to 5.
    for i in range(1, 6):
        # product(vowels, repeat=i) produces all possible i-length tuples of vowels.
        words_list.extend([''.join(p) for p in product(vowels, repeat=i)])

    # Sort the words lexicographically (dictionary order).
    words_list.sort()

    # Find the position (1-indexed) of the given word.
    # Alternatively, you can return words_list.index(word) + 1.
    return words_list.index(word) + 1


# Example test cases:
print(solution("AAAAE"))  # Expected output: 6
print(solution("AAAE"))   # Expected output: 10
print(solution("I"))      # Expected output: 1563
print(solution("EIO"))    # Expected output: 1189
