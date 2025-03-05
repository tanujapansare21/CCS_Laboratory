import math

# Prime number checking function
def is_prime(p):
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True


p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

if not is_prime(p) or not is_prime(q):
    print("Both numbers must be prime. Exiting...")
    exit()

n = p * q
phi = (p - 1) * (q - 1)

print("n =", n)
print("Φ(n) =", phi)


def find_e(phi):
    for e in range(2, phi):
        if math.gcd(phi, e) == 1:  
            return e
    return None  

#e
e = find_e(phi)
if e is None:
    print("No valid 'e' found")
    exit()

print(f"e = {e}")

def compute_d(e, phi):
    return pow(e, -1, phi)  

d = compute_d(e, phi)
print(f"d = {d}")

msg = int(input("Enter a number to encrypt (msg): "))

if msg >= n:
    print("Message must be smaller than n. Exiting...")
    exit()

print(f'Original message: {msg}')

# Encryption
C = pow(msg, e, n)  
print(f'Encrypted message: {C}')

# Decryption
M = pow(C, d, n)  
print(f'Decrypted message: {M}')
