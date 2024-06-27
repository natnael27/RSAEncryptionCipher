import random
import math

# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Find the greatest common divisor of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Find the multiplicative inverse of a number modulo m
def multiplicative_inverse(e, m):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_m = m
    while e > 0:
        temp1 = temp_m // e
        temp2 = temp_m - temp1 * e
        temp_m = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_m == 1:
        return d + m

# Generate random prime numbers
def generate_primes():
    p = random.randint(100, 1000)
    while not is_prime(p):
        p = random.randint(100, 1000)
    q = random.randint(100, 1000)
    while not is_prime(q) or q == p:
        q = random.randint(100, 1000)
    return p, q

# Generate public and private keys
def generate_keys():
    p, q = generate_primes()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi - 1)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi - 1)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)

# Encrypt a message using the public key
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Decrypt a message using the private key
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

# Example usage
public_key, private_key = generate_keys()
message = "NATNAEL"
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)
print("Original message: ", message)
print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)
