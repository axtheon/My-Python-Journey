list = ["Apple", "Orange", "Abdullah", "Saeed", "Khan", 5, False, True, 38.0499]
print("Original list:")
print(list)

# As there are some functions in strings, there are also methods in lists.
# The difference is that most string functions return a new string and don't change the original,
# but list methods often modify the list in place.

# 1. append() - Adds an element to the end of the list
list.append("Mountain")
print("\nAfter append('Mountain'):")
print(list)

# 2. extend() - Adds multiple elements to the end of the list
list.extend(["River", 100])
print("\nAfter extend(['River', 100]):")
print(list)

# 3. insert() - Inserts an element at a specific position
list.insert(1, "Inserted")
print("\nAfter insert(1, 'Inserted'):")
print(list)

# 4. remove() - Removes the first occurrence of a value
list.remove("Apple")
print("\nAfter remove('Apple'):")
print(list)

# 5. pop() - Removes and returns an element at the given index (default is last)
last_item = list.pop()
print("\nAfter pop(), removed item:", last_item)
print(list)

first_item = list.pop(0)
print("\nAfter pop(0), removed item:", first_item)
print(list)

# 6. index() - Returns the index of the first occurrence of a value
index_of_khan = list.index("Khan")
print("\nIndex of 'Khan':", index_of_khan)

# 7. count() - Counts how many times a value appears
true_count = list.count(True)
print("\nCount of True:", true_count)

# 8. sort() - Sorts the list in ascending order (only works if all elements are of the same type)
# To demonstrate this, we need a new list with same-type elements
numbers = [5, 3, 8, 1, 10]
numbers.sort()
print("\nSorted numbers list:")
print(numbers)

# 9. reverse() - Reverses the order of the list (in place)
list.reverse()
print("\nAfter reverse():")
print(list)

# 10. copy() - Returns a shallow copy of the list
copied_list = list.copy()
print("\nCopied list:")
print(copied_list)

# 11. clear() - Removes all items from the list
list.clear()
print("\nAfter clear():")
print(list)
