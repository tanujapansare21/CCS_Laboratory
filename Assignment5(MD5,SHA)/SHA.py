import hashlib

# Take input from user
message = input("Enter a message to hash: ")

# Create SHA-1 hash object and update it with the message
sha1_hash = hashlib.sha1(message.encode())

# Get hexadecimal hash output
hashed_output = sha1_hash.hexdigest()

print(f"SHA-1 Hash: {hashed_output}")
