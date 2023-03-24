from cryptography.fernet import Fernet
import datetime

# Load the key from a file
with open('key.key', 'rb') as file:
    key = file.read()

# Encrypt the current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
fernet = Fernet(key)
encrypted_time = fernet.encrypt(current_time.encode())
decrypted_time = fernet.decrypt(encrypted_time).decode()

print("Encrypted date and time:", encrypted_time)
print("Decrypted date and time:", decrypted_time)