userinput = input("Enter your Paypal email address: ")
while "@" not in userinput or "." not in userinput:
    print("❌ Please enter a valid email address.")
    userinput = input("Enter your Paypal email address: ")

print("Thank you for your payment. Your order will be processed shortly.")

print(f"Paypal email address entered: {userinput}")