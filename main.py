import random
import string
import pyperclip

if __name__ == '__main__':
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    numbers = list(string.digits)
    special_characters = list(string.punctuation)
    lists = [lowercase_letters, uppercase_letters, numbers, special_characters]
    password = []
    length = 0
    max_length = 32

    while length < max_length:
        random_list = random.choice(lists)
        character = random.choice(random_list)
        password.append(character)
        pyperclip.copy(''.join(password))
        length += 1
