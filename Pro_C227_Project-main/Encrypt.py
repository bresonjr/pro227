print('Welcome')
print("Rules: Don't open it")

message = input('Enter the message you want to encrypt: ')
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = input("Enter an encryption key of your choice (at least 8 numbers long): ")

# Check if the key is at least 8 characters long
if len(key) < 8:
    print("The encryption key should be at least 8 numbers long.")
else:
    encrypt = ''

    for char in message:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = (position + int(key)) % len(alphabet)
            encrypt += alphabet[new_position]
        else:
            encrypt += char

    print('Encrypted Message:', encrypt)
    print('Encryption Key:', key)
