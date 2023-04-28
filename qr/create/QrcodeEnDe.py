from cryptography.fernet import Fernet
import qrcode
from io import BytesIO
from PIL import Image
import pyqrcode

# Generate a key
key = Fernet.generate_key()

# Save the key to a file
with open('key2.key', 'wb') as file:
    file.write(key)

# Load the key from a file
with open('key2.key', 'rb') as file:
    key = file.read()

# Encrypt the message
message = b"Hello World"
fernet = Fernet(key)
encrypted_message = fernet.encrypt(message)

print("Encrypted message:", encrypted_message)

# Generate a QR code image from the encrypted message
img = qrcode.make(encrypted_message)

# Convert the image to a bytes object
bytes_obj = BytesIO()
img.save(bytes_obj, format='PNG')
qr_code_image_bytes = bytes_obj.getvalue()

# Save the QR code image to a file
with open("qr_code.png", "wb") as f:
    f.write(qr_code_image_bytes)

# Load the image from the file and display it
qr_code_image = Image.open("qr_code.png")
qr_code_image.show()