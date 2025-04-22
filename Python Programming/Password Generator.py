import random
import string

digits = "0123456789"
letters = string.ascii_letters
punctuation = string.punctuation

def password(length):
    password = ""
    while(length > 0):
        char = random.choice(digits + letters + punctuation)
        length -= 1
        password += char
    return password

print("Welcome to the password generator!")
while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Length must be a positive integer.")
            continue
        generated_password = password(length)
        print("Generated password:", generated_password)
        print("Do you want to generate another password? (y/n)")
        choice = input().strip().lower()
        if choice == 'n':
            print("Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
