import string
import random
def generate_password(length: int):
    
    if  length < 5:
        length = 5
    elif length > 20:
        length = 20

    characters = string.ascii_letters + string.digits + string.punctuation

    password ='' .join(random.choice(characters)for _ in range(length))
    return password
                       

print(generate_password(10))
