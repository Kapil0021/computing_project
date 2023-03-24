from cryptography.fernet import Fernet
import pyqrcode
import datetime

with open('key.key', 'rb') as file:
    key = file.read()

#get current time
currentTime = datetime.datetime.now()
#add 10 seconds to current time
currentTimeWithBuffer = currentTime + datetime.timedelta(0,10)
#print the time
print(currentTime,"-",currentTimeWithBuffer)
currentTimeWithBufferStr = str(currentTimeWithBuffer)
currentTimeWithBufferStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
fernet = Fernet(key)
encrypt_currentTime = fernet.encrypt(currentTimeWithBufferStr.encode())
#Account Number
accountNumber = '108000'
encrypted_integer = fernet.encrypt(str(accountNumber).encode())
#Device to make sure the transaction availablity
transactionState='True'

qr_data = f"{encrypt_currentTime} || {encrypted_integer} || {transactionState}"
#print the time
print(qr_data)

url = pyqrcode.create(qr_data)
#save the png file naming "qr.png"
url.png('qr.png', scale = 6)

decrypt_currentTime = fernet.decrypt(encrypt_currentTime.decode())
print(decrypt_currentTime)