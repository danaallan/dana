import random as rnd
import string


def generate_random_password(length):
    password = ''
    # random characters and number
    for _ in range(length):
        password += rnd.choice(string.ascii_letters + string.digits + string.punctuation)

    return password


length = int(input('Enter the length of the password: '))
num_passwords = int(input('Enter the number of passwords: '))

for i in range(num_passwords):
    print(generate_random_password(length))
print(string.ascii_letters)
#danaallan