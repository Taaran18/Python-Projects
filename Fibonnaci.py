# Get user input for the number of terms in the Fibonacci sequence
nterms = int(input("Enter the nth terms:"))

# Initialize the first two terms of the Fibonacci sequence
n1 = 0
n2 = 1

# Initialize a counter
count = 0

# Check if the input is a positive integer
if nterms <= 0:
    print("Enter a positive integer.")
elif nterms == 1:
    # If only one term is requested, print the first term
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
else:
    # Print the Fibonacci sequence up to the nth term using a while loop
    print("Fibonacci sequence up to", nterms, ":")
    while count < nterms:
        print(n1, end=",")  # Print the current term and separate with a comma
        nth = n1 + n2  # Calculate the next term
        n1 = n2  # Update n1 with the value of n2
        n2 = nth  # Update n2 with the value of nth
        count += 1  # Increment the counter
