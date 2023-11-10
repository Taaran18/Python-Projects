# Input n and x values from the user
n = int(input("Enter the n Value of the number: "))
x = int(input("Enter the x Value of the number: "))

# Initialize the sum to 1 (for the first term in the series)
s = 1

# Loop through the range from 1 to x (inclusive)
for i in range(1, x + 1):
    # Add the next term to the sum (n raised to the power of i)
    s = s + (n ** i)

# Print the final sum
print("Sum of the series:", s)
