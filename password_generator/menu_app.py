import console_app


def menu():

    while True:
        print("\nMENU\n\n")
        print("1. generate a password\n2. view archive\n3. clear archive\n4. exit")

        choice = int(input("what do you want to do? : "))
        print("\n")

        if choice == 4:
            break
        elif choice == 1:
            console_app.password_code()
        elif choice == 2:
            show_archive()
        elif choice == 3:
            clear_archive()


def show_archive():
    print("ARCHIVE\n")
    file = open('archive.txt', 'r')
    text = file.read()
    print(text)
    file.close()


def clear_archive():
    file = open('archive.txt', 'w')
    file.write("")
    file.close()
    print("\narchive cleared\n")


menu()
