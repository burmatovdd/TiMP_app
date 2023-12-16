from tkinter import *
from db import DataBase
from tkinter import filedialog
from tkinter.messagebox import showinfo


def openWindow(*args):
    window = Tk()
    window.title("Добавить нового химика")
    window["bg"] = "#1C1A3F"
    window.minsize(450, 225)

    frame = Frame(
        window,
        padx=10,
        pady=10,
        height=100,
        bg="#5E47E3",
    )
    frame.pack(expand=True)

    user_info = Label(
        frame,
        text="Введите ФИО химика",
        bg="#5E47E3",
        fg="#fff",
    )
    user_info.grid(row=0, column=0)

    user_entry = Entry(
        frame,
        background="#302D62",
        foreground="#fff"
    )
    user_entry.grid(row=1, column=0, padx=5)

    info_info = Label(
        frame,
        text="Введите описание химика",
        bg="#5E47E3",
        fg="#fff",
    )
    info_info.grid(row=0, column=1)

    info_entry = Entry(
        frame,
        background="#302D62",
        foreground="#fff"
    )
    info_entry.grid(row=1, column=1, padx=15)

    user_button = Button(
        frame,
        text="Добавить",
    )
    user_button.grid(row=1, column=2)
    user_button.bind('<Button-1>', lambda event: adduser([user_entry.get(), info_entry.get(), choose_img()], window))

    window.mainloop()

def choose_img():
    filename = filedialog.askopenfilename(title="Выбрать фотографию", initialdir="/",filetypes=[
        ('PNG pictures', '*.png'),
    ])
    if filename:
        print(filename)
        return filename
    return None

def adduser(data, window):
    print("in add user")
    print("data: ", data)
    database = DataBase("INSERT INTO personalities (fio , info , image) VALUES (?, ?, ?)")
    database.insert(data)
    showinfo(title="Памятка",
             message="Данные успешно добавлены")
    window.destroy()
