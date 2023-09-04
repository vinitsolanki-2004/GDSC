import random
import string


def pass_generate(length, special_chars):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return

    characters = string.ascii_letters + string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters)
                       for i in range(length))
    return password


def main():
    length = int(input("Enter desired password length: "))
    special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = pass_generate(length, special_chars)
    print("Generated password:", password)


if __name__ == "__main__":
    main()
