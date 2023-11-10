# Get input from the user
line = input("Enter the line: ")

# Initialize counters for various character types
lowercount = uppercount = digitcount = alphacount = spacecount = special = 0

# Iterate through each character in the input line
for a in line:
    # Check if the character is a lowercase letter
    if a.islower():
        lowercount += 1
    # Check if the character is an uppercase letter
    elif a.isupper():
        uppercount += 1
    # Check if the character is a digit
    elif a.isdigit():
        digitcount += 1
    # Check if the character is an alphabet letter (uppercase or lowercase)
    elif a.isalpha():
        alphacount += 1
    # Check if the character is a space
    elif a.isspace():
        spacecount += 1
    # If the character doesn't fall into any of the above categories, consider it special
    else:
        special += 1

# Print the counts for each character type
print("No. of uppercase letters:", uppercount)
print("No. of lowercase letters:", lowercount)
print("No. of digitcase letters:", digitcount)
print("No. of alphacase letters:", alphacount)
print("No. of spacecase letters:", spacecount)
print("No. of specialcase letters:", special)
