import string
import random
import base64
from cryptography.fernet import Fernet

# Generate a strong, unique password
def generate_password(length=16):
  # Use a combination of letters, numbers, and special characters
  characters = string.ascii_letters + string.digits + string.punctuation
  return ''.join(random.choice(characters) for i in range(length))

# Encrypt a password using a key
def encrypt_password(password, key):
  fernet = Fernet(key)
  encrypted_password = fernet.encrypt(password.encode())
  return encrypted_password

# Decrypt a password using a key
def decrypt_password(encrypted_password, key):
  fernet = Fernet(key)
  decrypted_password = fernet.decrypt(encrypted_password).decode()
  return decrypted_password

# Store a password for a specific website
def store_password(website, username, password, key):
  encrypted_password = encrypt_password(password, key)
  # Store the encrypted password in a file or a database
  with open('passwords.txt', 'a') as f:
    f.write(f'{website},{username},{encrypted_password}\n')

# Retrieve a password for a specific website
def retrieve_password(website, username, key):
  # Read the password file or query the database
  with open('passwords.txt', 'r') as f:
    for line in f:
      website_, username_, encrypted_password = line.strip().split(',')
      if website == website_ and username == username_:
        password = decrypt_password(encrypted_password, key)
        return password
  return None

# Check the strength of a password
def check_password_strength(password):
  # Check the length of the password
  if len(password) < 8:
    return 'Weak: Password is too short'
  # Check if the password contains a combination of letters, numbers, and special characters
  if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(char in string.punctuation for char in password):
    return 'Weak: Password is not complex enough'
  return 'Strong: Password is strong'

# Generate a key to encrypt and decrypt passwords
key = base64.urlsafe_b64encode(Fernet.generate_key())

# Generate a new password for a website
website = 'example.com'
username = 'user'
password = generate_password()
print(f'New password for {website}: {password}')

# Store the password
store_password(website, username, password, key)

# Retrieve the password
retrieved_password = retrieve_password(website, username, key)
print(f'Retrieved password for {website}: {retrieved_password}')

# Check the strength of the password
password_strength = check_password_strength(password)
print(f'Password strength: {password_strength
