import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    print("Welcome to the Strong Password Generator!")
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            length = int(input("Enter the length of each password: "))
            if num_passwords <= 0 or length <= 0:
                print("Please enter valid numbers for passwords and length.")
                continue
            break
        except ValueError:
            print("Please enter valid numbers for passwords and length.")

    passwords = generate_multiple_passwords(num_passwords, length)

    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password {idx}: {password}")

if __name__ == "__main__":
    main()
