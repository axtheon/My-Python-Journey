import os

# Specify the directory path
path = '/'  # Current directory

# Get the list of all files and directories
entries = os.listdir(path)

print(f"Contents of directory '{path}':")
for entry in entries:
    print(entry)
