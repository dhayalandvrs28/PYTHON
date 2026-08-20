# 3. Online Shopping Cart
def calculate_total(cus_name, ord_no, items, tax=0, discount=0, **add_charges):

    # Calculate the total MRP of items
    total_mrp = sum(price for name, price in items)

    # Apply discount
    total_after_discount = total_mrp - (total_mrp * (discount / 100))

    # Apply tax
    total_after_tax = total_after_discount + (total_after_discount * (tax / 100))

    # Add additional charges
    total_additional_charges = sum(add_charges.values())
    total_final = total_after_tax + total_additional_charges

    # Print the details
    print(f"\nCustomer Name: {cus_name}")
    print(f"Order Number: {ord_no}")
    print("Items:")
    for name, price in items:
        print(f"  - {name}: ${price:.2f}")
    print(f"Total Amount Payable: ${total_final:.2f}")

# Get user input
cus_name = input("Enter customer name: ")
ord_no = input("Enter order number: ")

# Get items from the user
items = []
while True:
    item_name = input("Enter item name (or type 'done' to finish): ")
    if item_name.lower() == 'done':
        break
    item_price = float(input(f"Enter price for {item_name}: "))
    items.append((item_name, item_price))

# Get tax and discount
tax = float(input("Enter tax percentage (e.g., 5 for 5%): "))
discount = float(input("Enter discount percentage (e.g., 10 for 10%): "))

# Get additional charges
additional_charges = {}
while True:
    charge_name = input("Enter additional charge name (or type 'done' to finish): ")
    if charge_name.lower() == 'done':
        break
    charge_value = float(input(f"Enter value for {charge_name}: "))
    additional_charges[charge_name] = charge_value

# Calculate and print the total
calculate_total(cus_name, ord_no, items, tax, discount, **additional_charges)
