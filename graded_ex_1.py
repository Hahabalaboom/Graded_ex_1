products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    sorted_list = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))
    return sorted_list

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    print("Categories:")
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    
    try:
        choice = input("Select a category by number: ")
        choice = int(choice) - 1
        if 0 <= choice < len(products):
            return choice
        else:
            print("Invalid choice. Please select a valid category number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    for product, price, quantity in cart:
        cost = price * quantity
        print(f"{product} - ${price} x {quantity} = ${cost}")
        total_cost += cost
    print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def main():
    while True:
        name = input("Enter your name (first and last name): ")
        if validate_name(name):
            break
        print("Invalid name. Please enter your first and last name.")

    while True:
        email = input("Enter your email address: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email address.")

    cart = []
    total_cost = 0

    while True:
        category_index = display_categories()
        category_name = list(products.keys())[category_index]
        category_products = products[category_name]
        
        while True:
            print(f"Products in {category_name}:")
            display_products(category_products)
            print("1. Select a product to buy")
            print("2. Sort the products by price")
            print("3. Go back to categories")
            print("4. Finish shopping")
            choice = input("Select an option: ")

            if choice == "1":
                try:
                    product_index = int(input("Enter product number: ")) - 1
                    if 0 <= product_index < len(category_products):
                        product = category_products[product_index]
                        quantity = int(input("Enter quantity: "))
                        if quantity > 0:
                            add_to_cart(cart, product, quantity)
                            total_cost += product[1] * quantity
                        else:
                            print("Quantity must be greater than zero.")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
            
            elif choice == "2":
                sort_order = input("Sort by price: ascending (1) or descending (2)? ")
                sort_order = "asc" if sort_order == "1" else "desc"
                category_products = display_sorted_products(category_products, sort_order)

            elif choice == "3":
                break

            elif choice == "4":
                if cart:
                    display_cart(cart)
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time.")
                return

if __name__ == "__main__":
    main()
