import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        print("Error: No character types selected.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
