import password_gui_code
from tkinter import *


def password_gui():

    root = Tk()

    root.title("password generator")

    # methods

    def create_password():

        global password_label

        power = int(power_data.get())
        digits = int(digits_data.get())

        upper = bool(upper_data.get())
        symbols = bool(symbols_data.get())

        password_variable = password_gui_code.generate_password(power, digits, upper, symbols)

        file = open('archive.txt', 'a')
        file.write(password_variable + "\n")
        file.close()

        # password_label = Label(root, text=password_variable)
        # password_label.grid(row=7, column=1)

        text = Text(root, height=2, width=20)
        text.insert(INSERT, str(password_variable))
        text.grid(row=7, column=1)

        return

    def open_archive():
        window1 = Tk()
        window1.title("password archive")

        file = open('archive.txt', 'r')
        text_var = file.read()

        # text_label = Label(window1, text=text_var)
        # text_label.grid(row=0)

        text = Text(window1, width=20)
        text.insert(INSERT, str(text_var))
        text.grid(row=0)

        window1.mainloop()
        file.close()

    def clear_archive():
        file = open('archive.txt', 'w')
        file.write("")
        file.close()

    # labels

    title_label = Label(root, text="----------(Password Generator)----------", bg="black", fg="green")
    title_blank_column = Label(root, text="-----------------------------", bg="black", fg="green")
    power_label = Label(root, text="password power:")
    digits_label = Label(root, text="digits:")
    upper_label = Label(root, text="uppercase letters:")
    symbols_label = Label(root, text="symbols:")
    blank_label = Label(root, text="===========================", fg="red")
    password_print_label = Label(root, text="password:")

    # entries and boxes

    power_data = IntVar()
    digits_data = IntVar()
    upper_data = BooleanVar()
    symbols_data = BooleanVar()

    power_entry = Entry(root, textvariable=power_data)
    digits_entry = Entry(root, textvariable=digits_data)
    upper_box = Checkbutton(root, onvalue=True, offvalue=False, variable=upper_data)
    symbols_box = Checkbutton(root, onvalue=True, offvalue=False, variable=symbols_data)

    # buttons
    sub_button = Button(root, text="GENERATE", command=create_password)
    show_button= Button(root, text="show password archive", command=open_archive)
    clear_button = Button(root, text="clear password archive", command=clear_archive)

    # girds

    title_label.grid(row=0)
    title_blank_column.grid(row=0, column=1)
    power_label.grid(row=2)
    digits_label.grid(row=3)
    upper_label.grid(row=4)
    symbols_label.grid(row=5)
    blank_label.grid(row=6)
    sub_button.grid(row=6, column=1)
    password_print_label.grid(row=7)
    show_button.grid(row=8)
    clear_button.grid(row=9)

    power_entry.grid(row=2, column=1)
    digits_entry.grid(row=3, column=1)
    upper_box.grid(row=4, column=1)
    symbols_box.grid(row=5, column=1)

    root.mainloop()

password_gui()
