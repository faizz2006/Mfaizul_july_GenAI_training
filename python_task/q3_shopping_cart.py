# q3_shopping_cart.py

cart = {}

def add_item(item, price, quantity=1):
    cart[item] = {
        "price": price,
        "quantity": quantity
    }

def display_cart():
    print("\n------ Shopping Cart ------")

    total = 0

    for item, details in cart.items():
        subtotal = details["price"] * details["quantity"]
        total += subtotal

        print(f"{item}")
        print(f"Price : ₹{details['price']}")
        print(f"Quantity : {details['quantity']}")
        print(f"Subtotal : ₹{subtotal}\n")

    print("Total Amount : ₹", total)


while True:
    print("\n===== Shopping Cart =====")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        item = input("Item Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        add_item(item, price, quantity)
        print("Item Added Successfully!")

    elif choice == "2":
        display_cart()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
