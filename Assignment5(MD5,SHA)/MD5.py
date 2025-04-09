import hashlib

# Input string
text = "Tanuja"

# Encode the string and generate MD5 hash
md5_hash = hashlib.md5(text.encode())

# Convert hash object to hexadecimal format
print("MD5 Hash:", md5_hash.hexdigest())
