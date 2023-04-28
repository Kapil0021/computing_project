from PIL import Image
from pyzbar.pyzbar import decode
from cryptography.fernet import Fernet

# Load the QR code image from a file
qr_code_image = Image.open("qr_code.png")

# Decode the QR code image and get the encrypted message
qr_code_data = decode(qr_code_image)[0].data
encrypted_message = qr_code_data.decode()

# Load the key from a file
with open('key2.key', 'rb') as file:
    key = file.read()

# Decrypt the message
fernet = Fernet(key)
decrypted_message = fernet.decrypt(encrypted_message.encode())

print("Decrypted message:", decrypted_message)