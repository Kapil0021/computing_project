import cv2
from cryptography.fernet import Fernet
import numpy as np

# Load the QR code image from file
qr_code_image = cv2.imread("qr_code.png")

# Create a QR code detector object
qr_code_detector = cv2.QRCodeDetector()

# Detect and decode the QR code
data, bbox, straight_qrcode = qr_code_detector.detectAndDecode(qr_code_image)

# Print the decoded data
print(data)
print(data.split('||')[0])
print(data.split('||')[1])
print(data.split('||')[2])
# Load the key from a file or generate a new one
with open('key1.key', 'rb') as file:
    key = file.read()

# Create a Fernet object with the key
fernet = Fernet(key)

# Decrypt the encrypted data
decrypted_data = fernet.decrypt(data.split('||')[0])
decrypted_data1 = fernet.decrypt(data.split('||')[1])
# Print the decrypted data
print(decrypted_data.decode())  
print(decrypted_data1.decode())

