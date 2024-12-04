import random
import string

def generate_password(length=12):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

    required_characters = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_symbols)
    ]

    remaining_length = length - len(required_characters)
    password_characters = required_characters + \
                          [random.choice(string.ascii_letters + string.digits + special_symbols)
                           for _ in range(remaining_length)]

    random.shuffle(password_characters)

    password = ''.join(password_characters)
    return password


def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)

    if length < 4:
        print("Error: Password length should be at least 4 characters.")
    else:
        generate_password()

        if password[0].isalpha() is True:
            print("Generated Password:", password)
        else:
            generate_password()

            if password.isdigit() is False:
                print("Sorry! There should be at least one digit in the password!")
                print("Try again!")
            else:
                print("Generated Password:", password)

if __name__ == "__main__":
    main()
