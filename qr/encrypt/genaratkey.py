from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Save the key to a file
with open('key.key', 'wb') as file:
    file.write(key)