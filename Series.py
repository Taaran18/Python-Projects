n = int(input("Enter the n Value of the number :"))
x = int(input("Enter the x Value of the number :"))
s = 1
for i in range(1, x + 1):
    s = s + (n ** i)
print(s)
