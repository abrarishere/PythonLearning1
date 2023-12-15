while True:
    term = int(input("Enter term to generate its table: "))
    quantity = int(input("Enter range: "))

    for value in range(quantity + 1):
        value_g = term * value
        print("---------------")
        print(f"{term} x {value} = {value_g}")
        print("---------------")

