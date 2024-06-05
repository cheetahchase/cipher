text = input("Enter message: ")
custom_key = input("Enter key: ")
code = input("Encrypt or decrypt: ")


def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    return vigenere(message, key)


def decrypt(message, key):
    return vigenere(message, key, -1)


if code == "decrypt" or code == "de":
    print(f'\nEncrypted text: {text}')
    print(f'Key: {custom_key}')
    decryption = decrypt(text, custom_key)
    print(f'\nDecrypted text: {decryption}\n')

if code == "encrypt" or code == "en":
    print(f'\nText: {text}')
    print(f'Key: {custom_key}')
    decryption = encrypt(text, custom_key)
    print(f'\nEncrypted text: {decryption}\n')
