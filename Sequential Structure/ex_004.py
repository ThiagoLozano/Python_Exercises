# Ex.004 Make a Program that asks for the 4 bimonthly notes and shows the average.
amount = 0

try:
    for b in range(1, 5):
        note = int(input(f"Note {b}: "))
        amount += note
    average = amount / 4
    print(f"\nAverage = {average}")
except Exception as error:
    print(f"Error: {error}")
