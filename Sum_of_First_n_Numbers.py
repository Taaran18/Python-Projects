# Get input from the user
num = int(input("Enter the Number: "))

# Initialize sum to 0
sum = 0

# Loop through numbers from 0 to num (inclusive) and calculate the sum
for i in range(0, num + 1, 1):
    sum = sum + i

# Print the result
print("Sum of First", num, "Numbers are:", sum)
