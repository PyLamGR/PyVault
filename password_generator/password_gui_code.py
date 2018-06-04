import random


def generate_password(power, digits, uppercase, symbols):

    password_list = []
    digit = ""
    chars = "abcdefghijklmnopqrstuvwxyz"

    if power != 0:

        if digits != 0:
            digit += "0123456789"

        if uppercase is True:
            chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if symbols is True:
            chars += "!@#$%^&*()_+-=,./;[]<>?:{}`~"

        for i in range(0, power-digits):
            choice = random.choice(chars)
            password_list.append(choice)

        for i in range(power-digits, power):
            dig = random.choice(digit)
            password_list.append(dig)

        password = ''.join(password_list)

    else:
        password = ""

    return password     # MUST SAVE PASSWORD TO A TXT FILE
