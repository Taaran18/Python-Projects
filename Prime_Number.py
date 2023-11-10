# Get user input for a number
num = int(input("Enter number: "))

# Calculate the limit for checking prime
lim = int(num / 2) + 1

# Initialize a variable to check if the number is prime
is_prime = True

# Loop to check for factors
for i in range(2, lim):
    rem = num % i

    if rem == 0:
        # If the remainder is zero, the number is not prime
        is_prime = False
        print(num, "is not a prime number.")
        break

# Check the prime status and print the result
if is_prime:
    print(num, "is a prime number.")
