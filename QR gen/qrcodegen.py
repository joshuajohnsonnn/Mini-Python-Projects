import qrcode

user_input = input("Enter the text or URL to generate a QR code: ")

qrobject = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qrobject.add_data(user_input)
qrobject.make(fit=True)

img = qrobject.make_image(fill_color="black", back_color="white")

img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")