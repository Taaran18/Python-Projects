# Outer loop for the number of rows (0 to 4)
for i in range(5):
    # Inner loop for the number to be printed in each row
    for j in range(1, i + 1):
        # Print the current value of 'i' without a newline character
        print(i, end="")

    # Move to the next line after printing the numbers for the current row
    print()