'''
Encryption for a passcode using Fernet Library
'''

from cryptography.fernet import Fernet

# Generate a key, open a file 'key.key' and write the key there
key = Fernet.generate_key()
with open('key.key','wb') as file:
    file.write(key)

# Opens 'key.key' and assigns the key stored there as 'key'
with open('key.key','rb') as file:
    key = file.read()

# Opens your json and reads data into a new variable called 'data'
# Store the key as {"KEY":{"YOUR_KEY"}}
with open('key_file.json','rb') as f:
    data = f.read()

# Encrypts data from your json
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

# Writes your encrypted key into a new JSON file
with open('key_file.json','wb') as f:
    f.write(encrypted)