# Outer loop for the number of rows (1 to 4)
for i in range(1, 5):
    # Inner loop for the number of '*' in each row
    for j in range(1, i):
        # Print '*' without a newline character
        print("*", end="")

    # Move to the next line after printing '*' for the current row
    print()