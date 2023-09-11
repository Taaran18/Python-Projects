line = input("Enter the line :")
lowercount = uppercount = digitcount = alphacount = spacecount = special = 0
for a in line:
    if a.islower():
        lowercount += 1
    elif a.isupper():
        uppercount += 1
    elif a.isdigit():
        digitcount += 1
    elif a.isalpha():
        alphacount += 1
    elif a.isspace():
        spacecount += 1
    else:
        special = special + 1

print("No. of uppercase letters :", uppercount)
print("No. of lowercase letters :", lowercount)
print("No. of digitcase letters :", digitcount)
print("No. of alphacase letters :", alphacount)
print("No. of spacecase letters :", spacecount)
print("No. of specialcase letters :", special)
