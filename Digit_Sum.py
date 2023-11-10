# Get user input for a number
num = int(input("Enter the number: "))
Sum = 0

# Calculate the sum of digits in the number
while num > 0:
    # Extract the last digit of the number
    Reminder = num % 10
    # Add the digit to the running sum
    Sum = Sum + Reminder
    # Remove the last digit from the number
    num = num // 10

# Print the sum of the digits
print("Sum of the digits of Given Number = %d" % Sum)
