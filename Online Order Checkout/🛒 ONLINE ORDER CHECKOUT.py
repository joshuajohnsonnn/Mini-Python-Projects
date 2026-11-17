from email.headerregistry import Address

print("=" * 40)
print("       🛒 ONLINE ORDER CHECKOUT")
print("=" * 40)

### Get order value
while True:
    try:
        order_value = float(input("💰 Enter the amount you spent: $"))
        print("❌ Amount cannot be negative." if order_value < 0 else "✅ Amount accepted.")
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
        DELIVERY_COST = 3.49
        break

    elif delivery_choice == "2":
        delivery = "Next Day Delivery"
        DELIVERY_COST = 4.99
        break

    else:
        print("❌ Please choose 1 or 2.")

###### Free standard delivery over $20
if order_value >= 20 and delivery_choice == "1":
    DELIVERY_COST = 0
    delivery = "Standard Delivery (FREE)"

TOTAL = order_value + DELIVERY_COST

Address = input("\n🏠 Enter your delivery address: ")

Payment_Method = input("💳 Enter your payment method (e.g., Credit Card, PayPal): ")

if Payment_Method.lower() == "paypal":
    import paypalpayment
else:
    import cardpayment
## Receipt details
print("\n" + "=" * 40)
print("             🧾 RECEIPT")
print("=" * 40)

print(f"Order Value:      ${order_value:.2f}")
print(f"Delivery:         {delivery}")
print(f"Delivery Cost:    ${DELIVERY_COST:.2f}")
print("-" * 40)
print(f"TOTAL:             ${TOTAL:.2f}")
print(f"VAT(20%) Included: ${TOTAL * 0.2:.2f}")
print("=" * 40)

#--

print("✅ Thank you for your order!")
print(f"📦 Your order will be delivered to: {Address}")
print(f"💳 Payment Method: {Payment_Method}")
if Payment_Method.lower() == "paypal":
    print(f"Paypal email address entered: {paypalpayment.userinput}")
else:
    print("Payment details entered:")
    print(f"Cardholder Name: {cardpayment.cardholder_name}")
    print(f"Card Number: {cardpayment.card_number}")
    print(f"Expiry Date: {cardpayment.expiry_date}")
    print(f"Sort Code: {cardpayment.sort_code}")
    print(f"CVV: {cardpayment.cvv}")