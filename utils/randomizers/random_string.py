import random
import string

def generate_random_string(length):
    """Generates a random string of fixed length using ASCII letters."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))