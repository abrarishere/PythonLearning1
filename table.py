while True:
    value      = int(input("Enter a number to print table(q to quit): "))
    rangetable = int(input("Enter a range to generate table: "))
    if value == "q":
        break
    else:
        for i in range(1, rangetable + 1):
            print(f"{value} x {i} = {value * i}")