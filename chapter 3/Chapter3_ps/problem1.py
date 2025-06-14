# 🟢 Basic Case & Whitespace Functions
text = "  Hello World  "
print(text.lower())       # '  hello world  '
print(text.upper())       # '  HELLO WORLD  '
print(text.capitalize())  # '  hello world  '
print(text.title())       # '  Hello World  '
print(text.strip())       # 'Hello World'
print(text.lstrip())      # 'Hello World  '
print(text.rstrip())      # '  Hello World'

# 🔍 Search & Replace
s = "banana"
print(s.find("a"))        # 1
print(s.index("n"))       # 2
print(s.count("a"))       # 3
print(s.replace("a", "@")) # 'b@n@n@'

# 📐 Checks
print("abc".isalpha())    # True
print("123".isdigit())    # True
print("abc123".isalnum()) # True
print("   ".isspace())    # True
print("hello".islower())  # True
print("HELLO".isupper())  # True
print("banana".startswith("ban"))  # True
print("banana".endswith("na"))     # True

# 🧩 Split & Join
csv = "a,b,c"
print(csv.split(","))           # ['a', 'b', 'c']
print(csv.rsplit(",", 1))       # ['a,b', 'c']
print("key:value".partition(":")) # ('key', ':', 'value')
print("-".join(['1', '2', '3']))  # '1-2-3'

# 🧠 Miscellaneous
print(len("hello"))        # 5
print("42".zfill(5))       # '00042'
print("hi".center(6))      # '  hi  '
