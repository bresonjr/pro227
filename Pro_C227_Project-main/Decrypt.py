print('Welcome')
import random

# Generate a random encryption key
keygen = random.randint(11111111111, 999999999999999)
print("Your encryption key:", keygen)

message = input('Enter the message you want to encrypt or decrypt: ')
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = int(input("Enter the encryption/decryption key: "))
output = ''

for char in message:
    if char in alphabet:
        position = alphabet.find(char)
        new_position = (position + key) % len(alphabet)
        output += alphabet[new_position]
    else:
        output += char

print('Encrypted/Decrypted message:', output)
