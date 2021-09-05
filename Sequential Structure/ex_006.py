# Ex.006 Make a program that asks for the radius of a circle, calculate and show its area.

try:
    r = float(input("Enter the value in radius: "))
    a = 3.14 * (r ** 2)
    print(f"The area is {a}")
except Exception as error:
    print(f"Error: {error}")
