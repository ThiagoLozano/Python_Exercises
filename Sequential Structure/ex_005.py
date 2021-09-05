# Ex.005 Make a Program that converts meters to centimeters.

try:
    m = int(input("Enter the value in meters: "))
    c = m * 100
    print(f"{m}m = {c}cm")
except Exception as error:
    print(f"Error: {error}")
