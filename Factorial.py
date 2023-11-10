# Get user input for a number
num = int(input("Enter the Number: "))
fact = 1  # Initialize factorial to 1

# Check if the number is zero or negative
if num <= 0:
    print("The Factorial of 0 is 1.")
else:
    # Calculate the factorial using a for loop
    for i in range(1, num + 1):
        fact = fact * i  # Multiply the current factorial by the current value of i

    # Print the result
    print("The factorial of", num, "is", fact)
