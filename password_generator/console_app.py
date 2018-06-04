import random
import os


def password_code():

    password_list = []

    def read_digits():

        try:
            digits = int(input("Digits: "))
        except ValueError:
            print("Enter an integer!\n")

        return digits

    def read_password_length():

        try:
            power = int(input("Password Power(Enter how many elements you want the password to have): "))
        except ValueError:
            print("Enter an integer!\n")

        return power

    def read_range_of_char():

        try:
            upper_case_input = str(input("Do you want the password to have uppercase letters? (y/n): "))
        except ValueError:
            print("Enter a char!\n")

        try:
            symbols_input = str(input("Do you want the password to have symbols other than the letters of the alphabet? (y/n): "))
        except ValueError:
            print("Enter a char!\n")

        if upper_case_input is 'y' and symbols_input is 'y':
            range_of_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=,./;\|[]<>?:`~"
        elif upper_case_input is 'y' and symbols_input is 'n':
            range_of_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif upper_case_input is 'n' and symbols_input is 'y':
            range_of_char = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=,./;\|[]<>?:`~"
        elif upper_case_input is 'n' and symbols_input is 'n':
            range_of_char = "abcdefghijklmnopqrstuvwxyz"
        else:
            print("Invalid Input!")
            exit(1)

        return range_of_char

    def generate_password():

        power = read_password_length()
        digits = read_digits()
        range_of_char = read_range_of_char()

        for i in range(0, power-digits):
            password_list.append(random.choice(range_of_char))
        for i in range(power-digits, power):

            number = str(random.randint(0, 9))
            password_list.append(number)

        password = ''.join(password_list)

        print("\n" + "password: " + password + "\n")

        file = open('archive.txt', 'a')
        file.write(password + "\n")
        file.close()

        return

    print("==========(PASSWORD_GENERATOR)==========")
    generate_password()

    os.system("pause")
