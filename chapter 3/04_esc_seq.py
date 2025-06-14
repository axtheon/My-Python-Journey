a = "Abdullah is a good boy\nbut not a bad boy!"
# it is a function used
# to seprate a lengthy
# line into two lines
print(a)
# there are some more of these as following

# 🔸 Common Escape Sequences in Python

print("Hello\tWorld")       # \t → Tab (horizontal space)
# Output: Hello    World

print("He said: \"Hi!\"")   # \" → Double quote
# Output: He said: "Hi!"

print('It\'s okay')         # \' → Single quote
# Output: It's okay

print("C:\\Users\\Name")    # \\ → Backslash
# Output: C:\Users\Name

print("First line\rSecond") # \r → Carriage return (overwrites line start)
# Output: Second line

print("Backspace\bTest")    # \b → Backspace
# Output: BackspacTest

print("Bell\a")             # \a → Bell sound (may trigger system alert)
# Output: (Triggers a sound if supported)

print("Form feed\fPage")    # \f → Form feed (used in printers)
# Output: Page appears on a new page (depends on environment)

print("Unicode: \u2764")    # \u → Unicode character (e.g., ❤️)
# Output: Unicode: ❤

print("Octal: \101")        # \ooo → Octal value (e.g., A)
# Output: Octal: A

print("Hex: \x41")          # \xhh → Hex value (e.g., A)
# Output: Hex: A
