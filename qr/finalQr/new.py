def custom_encrypt(message, key): 
    encrypted_message = '' 
    for char in message: 
        encrypted_message += chr(ord(char) + key) 
    return encrypted_message
message = "Kapil" 
key = 5

s = custom_encrypt (message, key)
print(s)