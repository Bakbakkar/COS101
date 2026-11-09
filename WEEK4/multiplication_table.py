# Display a multiplication table from 1 to 12.

number = int(input("Enter a whole number: "))
starting_multiplier = int(input("Enter the starting multiplier: "))
ending_multiplier = int(input("Enter the ending multiplier: "))
print()
print(f"MULTIPLICATION TABLE FOR {number}")
print("==============================")

for multiplier in range(starting_multiplier, ending_multiplier + 1):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")


