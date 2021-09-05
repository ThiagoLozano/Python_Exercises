# Ex.008 Make a Program that asks how much you earn per hour and the number of hours worked in the month.
# Calculate and show your total salary for that month.

try:
    ph = float(input("Enter how much you arn per hour: "))
    hw = int(input("Enter the number hours you worked in the month: "))
    salary = ph * hw
    print(f"Your salary is R${salary}")
except Exception as error:
    print(f"Error: {error}")
