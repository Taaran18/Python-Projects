# Get user input for a number
num = int(input("Enter a number: "))

# Initialize sum to 0
sum = 0

# Create a temporary variable to store the original number
temp = num

# Loop to calculate the sum of cubes of individual digits
while temp > 0:
    # Extract the last digit of the number
    digit = temp % 10
    # Add the cube of the digit to the sum
    sum += digit**3
    # Remove the last digit from the number
    temp //= 10

# Check if the original number is equal to the sum of cubes of its digits
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
