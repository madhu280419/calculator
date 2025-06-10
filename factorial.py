factorial = int(input("Enter first number: "))
count = 1
for i in range(1,factorial+1):
    count *= i
    print(count)