a = 6.5
print(type(a))
print(float(a))


a = float(input("Enter first number: "))
operator = input("Enter operator: ")
b = float(input("Enter second number: "))
if operator == "+":
    result = a + b
    print(result,end="")
elif operator == "-":
    result = a - b
    print(result,end="")