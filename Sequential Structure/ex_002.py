# Ex.002 Make a Program that asks for a number and then displays the message The number entered was [number].

try:
    number = int(input("Enter a number: "))
    print(f"The number entered was {number}.")
except Exception as error:
    print(f"Error: {error}")
