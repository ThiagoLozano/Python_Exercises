# Ex.009 Make a Program that asks for the temperature in degrees Fahrenheit, transform and show the temperature in degrees Celsius.

try:
    f = float(input("Enter temperature in degrees Fahrenheit: "))
    c = 5 * ((f - 32) / 9)
    print(f"{f}Fº = {c}Cº")
except Exception as error:
    print(f"Error: {error}")
