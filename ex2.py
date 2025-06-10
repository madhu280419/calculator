num_1 = int(input("Enter first number: "))
operator = input("Enter operator:")
num_2 = float(input("ENter second number: "))
if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator =="/":
    print(num_1 / num_2)
elif operator == "%":
    print(num_1 % num_2)
elif operator == "**":
    print(num_1 ** num_2)
elif operator == "//":
    print(num_1 // num_2)
else:
    print("invalid operator")