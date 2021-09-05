# Ex.010 Make a Program that asks for the temperature in degrees Celsius, transform and display in degrees Fahrenheit.

try:
    c = float(input("Enter temperature in degrees Celsius: "))
    f = (c * 1.8) + 32
    print(f"{c}Cº = {f}Fº")
except Exception as error:
    print(f"Error: {error}")
