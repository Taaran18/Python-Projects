nterms = int(input("Enter the nth terms:"))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
    print("Enter the Positive Integer:")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence upto", nterms, ":")
    while count < nterms:
        print(n1, end=',')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
