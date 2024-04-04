import random
import string

def generate_password(length):
    """Generate a random password with a given length"""
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for i in range(length))
    return password

# Example usage
print(generate_password(12))