print("=" * 40)
print("       🛒 ONLINE ORDER CHECKOUT")
print("=" * 40)

### Get order value
while True:
    try:
        order_value = float(input("💰 Enter the amount you spent: $"))
        print("❌ Amount cannot be negative." if order_value < 0 else "")
        if order_value < 0:
            continue
        break
    except ValueError:
        print("❌ Please enter a valid number.")

##### Delivery options
print("\n🚚 Delivery Options")
print("1. Standard Delivery - $3.49")
print("2. Next Day Delivery - $4.99")

while True:
    delivery_choice = input("\nChoose delivery (1 or 2): ")

    if delivery_choice == "1":
        delivery = "Standard Delivery" 
        delivery_cost = 3.49
        break

    elif delivery_choice == "2":
        delivery = "Next Day Delivery"
        delivery_cost = 4.99
        break

    else:
        print("❌ Please choose 1 or 2.")

###### Free standard delivery over $20
if order_value >= 20 and delivery_choice == "1":
    delivery_cost = 0
    delivery = "Standard Delivery (FREE)"

TOTAL = order_value + delivery_cost

## Receipt
print("\n" + "=" * 40)
print("             🧾 RECEIPT")
print("=" * 40)

print(f"Order Value:      ${order_value:.2f}")
print(f"Delivery:         {delivery}")
print(f"Delivery Cost:    ${delivery_cost:.2f}")
print("-" * 40)
print(f"TOTAL:            ${TOTAL:.2f}")
print("=" * 40)

print("✅ Thank you for your order!")