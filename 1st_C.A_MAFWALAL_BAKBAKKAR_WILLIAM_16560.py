while True:
    number = input("enter a whole number (e to end process):")
    print("===============================")
    if number == "e":
        print("ERROR")
        break
    number = int(number)
    print()
    if number <= 1:
        print("Please a enter number above 1!")
    else:
        for multiplication in range (1, 13):
            result = number * multiplication
            print(f"{number} * {multiplication} = {result}")
    
