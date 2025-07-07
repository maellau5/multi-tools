import random
import string

def generate_nitro_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(24))

if __name__ == "__main__":
    nitro_code = generate_nitro_code()
    print(nitro_code)