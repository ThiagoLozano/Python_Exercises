# Ex.007 Make a program that calculates the area of a square, then show twice this area to the user.

try:
    side = float(input("Enter the value in side: "))
    a = side ** 2
    print(f"Area = {a}cm²")
except Exception as error:
    print(f"Error: {error}")
