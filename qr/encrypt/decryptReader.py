from cryptography.fernet import Fernet

# Load the key from a file
with open('key.key', 'rb') as file:
    key = file.read()

# Decrypt the date and time
fernet = Fernet(key)
decrypted_time = fernet.decrypt(encrypt_currentTime).decode()
decrypted_time = fernet.decrypt(encrypted_integer).decode()


print("Decrypted date and time:", decrypted_time)