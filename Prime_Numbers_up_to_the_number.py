# Define the lower bound for the range
lower = 1

# Get user input for the upper bound of the range
upper = int(input("Enter upper range: "))

# Print a message indicating the range of prime numbers to be found
print("Prime numbers between 1 and", upper, "are:")

# Loop through the range of numbers from lower to upper
for num in range(lower, upper + 1):
    # Check if the current number is greater than 1
    if num > 1:
        # Nested loop to check for factors
        for i in range(2, num):
            # If a factor is found, break out of the loop
            if num % i == 0:
                break
        else:
            # If no factors are found, print the prime number
            print(num)
