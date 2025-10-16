
# Simple Bill Calculator

# Input: item details
item_name = input("Enter the item name: ")
price = float(input("Enter the price of one item: ₹"))
quantity = int(input("Enter the quantity: "))

# Constants
TAX_RATE = 0.05  # 5% tax

# Calculations
subtotal = price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

# Output: formatted bill
print("\n**")
print("🧾 SIMPLE BILL CALCULATOR")
print("")
print(f"Item Name : {item_name}")
print(f"Price     : ₹{price:.2f}")
print(f"Quantity  : {quantity}")
print(f"Subtotal  : ₹{subtotal:.2f}")
print(f"Tax (5%)  : ₹{tax:.2f}")
print("------------------------------")
print(f"Total Bill: ₹{total:.2f}")
print("")
print("✅ Thank you for shopping with us!")









