# Ex.003 Make a Program that asks for two numbers and prints the sum.

try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    s = n1 + n2
    print(f"{n1} + {n2} = {s}")
except Exception as error:
    print(f"Error: {error}")
