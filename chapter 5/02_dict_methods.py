# Some of the methods for Dictionaries are following:
a = {} # It is an empty Dictionary
marks = {
    "Abdullah": 100,
    "Ali": 84,
    "Ahmed": 26
}
print(marks.items()) # will print items in the dict separately
print(marks.keys()) # will print the keys used in dict
print(marks.values()) # will print the values of the keys in the dict
marks.update({"Abdullah": 95}) # will change the value of a key
print(marks)
# By using marks.update method we can also add a new key in the existing dictionary.
marks.update({"Hamza": 100})
print(marks)
print(marks.get("Abdullah")) # will print the marks of Abdullah
'''
In the previous file I used print(marks["Abdullah"]) and in this file I am using
print(marks.get("Abdullah")) this method. Yeah these are both used to do the same task
but if I used a key which doesn't exist in the dictionary the .get method will output
None but if we use print(marks["Abdullah"]) this method it will provide us an error.
FOR EXAMPLE:
print(marks.get("Ayesha")) : Output: None
print(marks["Ayesha"]) : Output: Error
'''