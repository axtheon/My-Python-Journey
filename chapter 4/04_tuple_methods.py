# Define a tuple with mixed data types
a = ("Apple", "Orange", "Abdullah", "Saeed", "Khan", 5, False, True, 38.0499)

# Print the entire tuple
print(a)

# count() method returns the number of times a specific value appears in the tuple
no = a.count("Abdullah")
print(no)

# index() method returns the first index at which a value is found
index_value = a.index("Abdullah")
print("Index of 'Abdullah':", index_value)

# len() function returns the total number of elements in the tuple
tuple_length = len(a)
print("Length of the tuple:", tuple_length)

# Using slicing to get a subset of the tuple
subset = a[1:4]
print("Sliced tuple (index 1 to 3):", subset)

# Membership test using 'in' to check if a value exists in the tuple
is_present = "Khan" in a
print("Is 'Khan' present in the tuple?:", is_present)

# Convert the tuple to a list to allow modifications (tuples are immutable)
a_list = list(a)
print("Converted to list for modification:",a_list)