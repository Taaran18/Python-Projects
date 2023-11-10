# Open the file 'new.txt' in read-only mode
myFile = open(r'new.txt', "r")

# Read the content of the file into a string
file_content = myFile.read()

# Calculate the size of the file (length of the string)
file_size = len(file_content)

# Print the size of the file in bytes
print("Size of the given file 'new.txt' is:")
print(file_size, "bytes")

# Close the file
myFile.close()
