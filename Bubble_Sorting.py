# Get user input for a list of integers separated by spaces
user_input = input("Enter a list of integers (space): ")

# Convert the input string to a list of integers
alist = [int(x) for x in user_input.split()]

# Print the original list
print("Original list is:", alist)

# Perform Bubble Sort to sort the list
n = len(alist)
for i in range(n):
    for j in range(0, n - i - 1):
        if alist[j] > alist[j + 1]:
            alist[j], alist[j + 1] = alist[j + 1], alist[j]

# Print the sorted list
print("List after sorting:", alist)
