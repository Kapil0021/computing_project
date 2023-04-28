import sqlite3
from pyfingerprint.pyfingerprint import PyFingerprint

# Connect to the fingerprint module
f = PyFingerprint('lsof | grep /dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

# Open the database
conn = sqlite3.connect('fingerprint_database.db')
c = conn.cursor()

# Create the fingerprint table
c.execute('''CREATE TABLE fingerprints
             (id INTEGER PRIMARY KEY,
             fingerprint_data BLOB)''')

# Function to enroll a fingerprint
def enroll_fingerprint():
    # Wait for a finger to be placed on the module
    while (f.readImage() == False):
        pass
    
    # Convert the image to a template
    f.convertImage(0x01)
    
    # Create a new fingerprint object
    fingerprint = bytearray(f.downloadCharacteristics())
    
    # Insert the fingerprint data into the database
    c.execute("INSERT INTO fingerprints (fingerprint_data) VALUES (?)", (fingerprint,))
    conn.commit()
    
    print("Fingerprint enrolled successfully.")

# Function to search for a fingerprint
def search_fingerprint():
    # Wait for a finger to be placed on the module
    while (f.readImage() == False):
        pass
    
    # Convert the image to a template
    f.convertImage(0x01)
    
    # Search for a match in the database
    result = f.searchTemplate()
    
    if (result == -1):
        print("Fingerprint not found.")
    else:
        print("Fingerprint found. ID: ", result)
    
# Main loop
while True:
    command = input("Enter command (enroll/search/exit): ")
    
    if (command == "enroll"):
        enroll_fingerprint()
    elif (command == "search"):
        search_fingerprint()
    elif (command == "exit"):
        break
    
# Close the database
conn.close()
