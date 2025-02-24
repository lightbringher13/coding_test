from functools import cmp_to_key
"""
What Does cmp_to_key Do?
	1.	Custom Comparator Function:
        The function custom_compare(a, b) compares 
        two elements (a and b). It returns:
	•	-1 if a should come before b 
        (for example, if the last character of a is 
        less than that of b, or if they are equal and 
        a is lexicographically less than b).
	•	1 if a should come after b.
	•	0 if a and b are considered equal.

	2.	Converting Comparator to Key Function:
        In Python 3, sorting functions like sorted() and 
        list.sort() accept a key parameter (a function that 
        extracts a value from each element to sort by), 
        but they no longer accept a comparator function directly.
        The cmp_to_key function from the functools module 
        converts a comparator function (like our custom_compare) 
        into a key function.
        What happens internally is that cmp_to_key(custom_compare) 
        returns a callable that wraps each element. These wrapped 
        elements know how to compare themselves with one another 
        by calling custom_compare on the underlying values.
        
	3.	Sorting Process:
        The sorted() function uses the key function produced 
        by cmp_to_key to order the items. Each item in the list 
        is wrapped, and when two wrapped items are compared, 
        Python internally calls your custom comparator to decide 
        their order.

Explanation of the Example
	•	Custom Comparison:
        For two strings a and b, we first compare a[-1] and b[-1] 
        (the last characters). For instance, comparing "apple" and 
        "banana":
	•	"apple"[-1] is "e", and "banana"[-1] is "a".
	•	Since "e" > "a", the comparator returns 1, 
        meaning "apple" should come after "banana".
	•	Lexicographical Tie-Breaker:
        If two strings have the same last character, 
        the code then falls back to a standard lexicographical 
        comparison (e.g., comparing "date" and "grape" 
        if both end with the same letter).
	•	Result:
        After sorting, the list sorted_words will be ordered 
        according to the rules defined in custom_compare.

        Running the code produces the sorted list of strings 
        based on their last character (and lexicographically when tied).

        This example demonstrates how cmp_to_key enables you 
        to use your custom comparator with Python’s sorting functions, 
        allowing you to control exactly how elements are compared 
        and ordered.
"""


def custom_compare(a, b):
    # Compare by the last character of each string.
    # If the last character of a is less than that of b, a comes first.
    if a[-1] < b[-1]:
        return -1
    elif a[-1] > b[-1]:
        return 1
    else:
        # If the last characters are equal, compare the strings normally (lexicographically).
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0


if __name__ == "__main__":

    # List of strings to sort.
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    # Use cmp_to_key to convert the comparator into a key function.
    sorted_words = sorted(words, key=cmp_to_key(custom_compare))
    print(sorted_words)
