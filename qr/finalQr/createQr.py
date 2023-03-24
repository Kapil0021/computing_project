from cryptography.fernet import Fernet
import qrcode
from io import BytesIO
from PIL import Image
import datetime

# Generate a key
key = Fernet.generate_key()

# Save the key to a file
with open('key1.key', 'wb') as file:
    file.write(key)

# Load the key from a file
with open('key1.key', 'rb') as file:
    key = file.read()

# Encrypt the message
currentTime = datetime.datetime.now()
# add 10 seconds to current time
currentTimeWithBuffer = currentTime + datetime.timedelta(0, 10)
# print the time
print(currentTime, "-", currentTimeWithBuffer)

currentTimeWithBufferStr = str(currentTimeWithBuffer)
currentTimeWithBufferStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
fernet = Fernet(key)
encrypt_currentTime = fernet.encrypt(currentTimeWithBufferStr.encode())

# Account Number
accountNumber = '108000'
encrypted_accnum = fernet.encrypt(str(accountNumber).encode())
# Device to make sure the transaction availability
transactionState = 'True'

# qr_data = f"{encrypt_currentTime.decode()} || {encrypted_accnum.decode()} || {transactionState}"

qr_data = encrypt_currentTime.decode() + "||" + encrypted_accnum.decode() + "||" + transactionState

# Generate a QR code image from the encrypted message
img = qrcode.make(qr_data)

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

#print the all data 
print(qr_data)
print(f"{currentTime} -{currentTimeWithBuffer} || {accountNumber} || {transactionState}")
