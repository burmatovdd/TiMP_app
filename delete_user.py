from tkinter import *
from db import DataBase
from tkinter.messagebox import showinfo


def openWindow(*args):
    window = Tk()
    window.title("Удалить химика")
    window["bg"] = "#695CFF"
    window.minsize(450, 225)

    frame = Frame(
        window,
        padx=10,
        pady=10,
        height=100,
        bg="#221F4A",
    )
    frame.pack(expand=True)

    delete_ino = Label(
        frame,
        text="Чтобы удалить химика, нажмите на его ФИО",
        bg="#221F4A",
        fg="#fff",
    )
    delete_ino.grid(row=0, column=1)

    database = DataBase("select * from personalities")
    users_info = database.select(None)
    users_list = Listbox(
        frame,
        bg="#221F4A",
        foreground="#fff",
        borderwidth=0,
        width=27
    )
    for user in users_info:
        users_list.insert(0,user[0])
    users_list.grid(row=2, column=1)
    users_list.bind('<<ListboxSelect>>', deleteUser)

    # user_button.grid(row=0, column=3)
    # user_button.bind('<Button-1>', lambda event: deleteUser())

    window.mainloop()


def deleteUser(event):
    widget = event.widget
    selection = widget.curselection()
    print("user: ", widget.get(selection[0]))
    database = DataBase("delete from personalities where fio = ?")
    database.exec([widget.get(selection[0])])
    showinfo(title="Памятка",
             message="Данные успешно удалены")

