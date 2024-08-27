import string
import random

def generate_password(length, use_special_chars=True):
    """Generate a random password with specified length and complexity."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Define the character sets to use
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all character sets
    all_chars = letters + digits + special_chars
    
    if not all_chars:
        raise ValueError("No characters available for password generation.")
    
    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    """Main function to run the password generator."""
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() in ['yes', 'y']
        
        if length < 1:
            print("Length must be at least 1.")
            return
        
        password = generate_password(length, use_special_chars)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
