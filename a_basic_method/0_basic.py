"""
1. List Methods and Techniques
	•	Appending and Extending:
	•	append(item): Adds an item to the end.
	•	extend(iterable): Adds all items from an iterable.
	•	Example:

    •	Removing Elements:
	•	pop(index): Removes and returns the element at the specified index (default is the last element).
	•	remove(item): Removes the first occurrence of the specified item.

    •	Sorting and Reversing:
	•	sort(key=..., reverse=...): Sorts the list in place.
	•	sorted(iterable, key=..., reverse=...): Returns a new sorted list.
	•	reverse(): Reverses the list in place.
	•	reversed(iterable): Returns an iterator over the elements in reverse order.
	•	Example:
    
    •	Slicing and Comprehensions:
	•	Slicing (lst[start:stop:step]) is a powerful way to access sublists.
	•	List comprehensions provide a concise way to create lists.
	•	Example:

2. Dictionary Methods and Techniques
	•	Basic Access and Modification:
	•	dict[key]: Access value.
	•	get(key, default): Get value with a default if key isn’t present.
	•	keys(), values(), items(): Return views of keys, values, or key-value pairs.
	•	update(other): Update dictionary with key-value pairs from another dictionary.
	•	pop(key, default): Remove and return the value for the key.
	•	Example:
    
3. String Methods
	•	Common Methods:
	•	split(), join(): For splitting a string into parts or joining a list of strings.
	•	strip(), lstrip(), rstrip(): Remove whitespace.
	•	replace(old, new): Replace substrings.
	•	lower(), upper(): Case conversion.
	•	find(), index(): Searching within strings.
	•	Example:

4. Set Methods
	•	Basic Set Operations:
	•	add(item), remove(item), discard(item): For adding or removing items.
	•	union(), intersection(), difference(), symmetric_difference(): For set operations.
	•	Methods like issubset() and issuperset() are also useful.
	•	Example:

5. Built-in Functions and Techniques
	•	sorted() and reversed():
        As discussed earlier, these functions are essential 
        for ordering and iterating in reverse.
	•	zip() and enumerate():
	•	zip(*iterables): Combine multiple iterables into tuples.
	•	enumerate(iterable, start=0): Get index-element pairs.
	•	Example:

    •	map(), filter(), and Lambda Functions:
	•	map(function, iterable): Apply a function to every element.
	•	filter(function, iterable): Filter elements based on a predicate.
	•	Lambdas allow you to write small anonymous functions.
	•	Example:
    
    •	List/Dictionary Comprehensions:
	•	Powerful one-line constructs to build lists, sets, or dictionaries.
	•	Example:

6. Standard Library Modules
	•	collections:
        Includes specialized container datatypes like Counter, 
        defaultdict, deque, and namedtuple.
	•	itertools:
        Provides tools for efficient looping, 
        like permutations, combinations, product, and more.
	•	math:
        Useful mathematical functions.
	•	bisect:
        For binary search in sorted lists.
"""
