def isEmpty(stk):
    # Check if the stack is empty
    if stk == []:
        return True
    else:
        return False


def Push(stk, item):
    # Push an item onto the stack
    stk.append(item)
    top = len(stk) - 1  # Update the top of the stack


def Pop(stk):
    # Pop an item from the stack
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None  # If the stack is empty, set top to None
        else:
            top = len(stk) - 1  # Update the top of the stack
        return item


def Peek(stk):
    # Peek at the top item of the stack without removing it
    if isEmpty(stk):
        return "Underflow"
    else:
        top = len(stk) - 1
        return stk[top]


def Display(stk):
    # Display the entire stack
    if isEmpty(stk):
        print("Stack empty")
    else:
        top = len(stk) - 1
        print(stk[top], "<-top")
        for a in range(top - 1, -1, -1):
            print(stk[a])


# ___main___
Stack = []  # Initialize an empty stack
top = None  # Variable to keep track of the top of the stack (not being used)

while True:
    print("STACK OPERATIONS")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display stack")
    print("5. Exit")

    ch = int(input("Enter the choice: "))

    if ch == 1:
        item = int(input("Enter item: "))
        Push(Stack, item)

    elif ch == 2:
        item = Pop(Stack)
        if item == "Underflow":
            print("Underflow! Stack is empty")
        else:
            print("Popped item is", item)

    elif ch == 3:
        item = Peek(Stack)
        if item == "Underflow":
            print("Underflow! Stack is empty")
        else:
            print("Topmost item is", item)

    elif ch == 4:
        Display(Stack)

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
