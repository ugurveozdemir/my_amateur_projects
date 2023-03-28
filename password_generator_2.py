import cs50
import string
import random
def generate_password():
    prompt = None
    print("Please type how many characters you want for password")
    while True:
        prompt = cs50.get_int('-->')
        if prompt < 8:
            print("It can not be less than 8 characters.")
            continue
        elif prompt > 32:
            print("It can not be more than 32 characters.")
            continue
        break
    password = ""
    while len(password) < prompt:
        random.shuffle(all_characters)
        for i in all_characters:
            password += random.choice(i)
    print(f"Your password is {password}")
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
all_characters = [lower_letters,upper_letters,digits,punctuation]

generate_password()