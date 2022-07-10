while True:
    try:
        count = int(input("enter count:"))
        price = int(input("enter price for each one:"))
        pay = count * price
        print("The price is: ", pay)
        break
    except ValueError:
        print("Error, enter numeric one.")
        