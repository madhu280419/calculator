num_1 =int(input("Enter first number: "))
operator = int(input("Enter operator: "))
num_2 =int(input("Enter second number: "))
if operator == "+":
    result = num_1 + num_2
    print(result)
elif operator == "-":
    result = num_1 - num_2
    print(result)
elif operator == "*":
    result = num_1 * num_2
    print(result)
elif operator == "/":
    result = num_1 / num_2
    print(result)