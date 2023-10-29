import itertools
import string


def get_user_password():
    password = input("Enter a password: ")
    return password


def crack_password(password):
    print("Starting brute-force attack to crack the password...")

    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    for password_length in range(1, len(password) + 1):
        for guess in itertools.product(characters, repeat=password_length):
            guess = ''.join(guess)
            if guess == password:
                return guess


def main():
    user_password = get_user_password()
    cracked_password = crack_password(user_password)
    if cracked_password:
        print(f"Password successfully cracked! It was: {cracked_password}")
    else:
        print("Failed to crack the password.")


if __name__ == "__main__":
    main()
