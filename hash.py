import hashlib

def encrypt_password(password):
    # Create a hash object using SHA-256 algorithm
    hash_object = hashlib.sha256(password.encode())
    # Get the hexadecimal representation of the hash
    hashed_password = hash_object.hexdigest()
    return hashed_password

# Example password
password =input("Enter Your password: \n")

# Encrypt the password
hashed_password = encrypt_password(password)

# Write the hashed password to password.txt
with open("password.txt", "w") as f:
    f.write(hashed_password)
