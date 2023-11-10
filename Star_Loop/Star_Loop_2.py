# Outer loop for the number of rows (0 to 4)
for i in range(5):
    # Inner loop for the number to be printed in each row
    for j in range(1, i):
        # Print the current value of 'j' without a newline character
        print(j, end="")

    # Move to the next line after printing the numbers for the current row
    print()