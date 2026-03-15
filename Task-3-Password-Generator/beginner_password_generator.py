import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# ---- User Input ----
try:
    length = int(input("Enter password length: "))
    
    if length <= 0:
        print("Length must be positive!")
        exit()

    print("Include letters? (yes/no)")
    use_letters = input().lower() == "yes"

    print("Include numbers? (yes/no)")
    use_numbers = input().lower() == "yes"

    print("Include symbols? (yes/no)")
    use_symbols = input().lower() == "yes"

    result = generate_password(length, use_letters, use_numbers, use_symbols)
    print("Generated Password:", result)

except ValueError:
    print("Please enter a valid number!")
