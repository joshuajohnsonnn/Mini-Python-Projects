cardholder_name = input("💳 Enter the Cardholder's name: ")
card_number = input("💳 Enter your Card number: ")
while card_number.isdigit() == False or len(card_number) != 16:
    print("❌ Please enter a valid 16-digit card number.")
    card_number = input("💳 Enter your Card number: ")
expiry_date = input("💳 Enter the Expiry date (MM/YY): ")
while len(expiry_date) != 5 or expiry_date[2] != '/':
    print("❌ Please enter a valid expiry date in the format MM/YY.")
    expiry_date = input("💳 Enter the Expiry date (MM/YY): ")
sort_code = input("💳 Enter your Sort code: ")
while sort_code.isdigit() == False or len(sort_code) != 6:
    print("❌ Please enter a valid 6-digit sort code.")
    sort_code = input("💳 Enter your Sort code: ")
cvv = input("💳 Enter the CVV: ")
while cvv.isdigit() == False or len(cvv) != 3:
    print("❌ Please enter a valid 3-digit CVV.")
    cvv = input("💳 Enter the CVV: ")

print("\n✅ Payment details received. Your order will be processed shortly.")

print("Payment details entered:")
print(f"Cardholder Name: {cardholder_name}")
print(f"Card Number: {card_number}")
print(f"Expiry Date: {expiry_date}")
print(f"Sort Code: {sort_code}")
print(f"CVV: {cvv}")


