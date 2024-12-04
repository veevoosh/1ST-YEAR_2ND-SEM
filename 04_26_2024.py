def caesar_cipher_encrypt():
    message = input("Enter the message to encrypt: ")
    shift_value = int(input("Enter shift value for encryption: "))
    cipher = ''
    for char in message:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + shift_value
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    print(cipher)


def caesar_cipher_decrypt():
    message = input("Enter the encrypted message to decrypt: ")
    shift_value = int(input("Enter shift value for decryption: "))
    text = ''
    for char in message:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - shift_value
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)
    print(text)


def main():
    print("Welcome to the Caesar Cipher Program!")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ")
    if choice == 'E' or choice == 'e':
        caesar_cipher_encrypt()
    elif choice == 'D' or choice == 'd':
        caesar_cipher_decrypt()
    else:
        print("Invalid choice! Please try again.")


main()
