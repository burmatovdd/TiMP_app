from tkinter import *
from db import DataBase
from tkinter import filedialog
from tkinter.messagebox import showinfo

def openWindow(*args):
    window = Tk()
    window.title("Изменить химика")
    window["bg"] = "#22A7DB"
    window.minsize(450, 225)

    frame = Frame(
        window,
        padx=10,
        pady=10,
        height=100,
        bg="#DB22BD",
    )
    frame.pack(expand=True)

    edit_info = Label(
        frame,
        text="Нажмитие на химика, которого хотите изменить",
        bg="#DB22BD",
        fg="#fff",
    )
    edit_info.grid(row=0, column=0)

    database = DataBase("select * from personalities")
    users_info = database.select(None)
    users_list = Listbox(
        frame,
        bg="#DB22BD",
        foreground="#fff",
        borderwidth=0,
        width=27
    )
    for user in users_info:
        users_list.insert(0, user[0])
    users_list.grid(row=1, column=0, pady=10)
    users_list.bind('<<ListboxSelect>>', editUser)


def editUser(event):
    widget = event.widget
    selection = widget.curselection()

    window = Tk()
    window.title(f"Изменение химика")
    window["bg"] = "#DB22BD"
    window.minsize(450, 225)

    frame = Frame(
        window,
        padx=10,
        pady=10,
        height=100,
        bg="#DB22BD",
    )
    frame.pack(expand=True)

    info = Label(
        frame,
        text="Оставьте поле пустым, если не хотите менять его",
        bg="#DB22BD",
        fg="#fff",
    )
    info.grid(row=0, column=0, columnspan=4)

    fio_info = Label(
        frame,
        text=f"Введите новое фио для {widget.get(selection[0])}",
        bg="#DB22BD",
        fg="#fff",
    )
    fio_info.grid(row=1, column=0, pady=10, padx=15)

    fio_entry = Entry(
        frame,
        background="#7E67E9",
        foreground="#fff"
    )
    fio_entry.grid(row=2, column=0, padx=15)

    desc_info = Label(
        frame,
        text=f"Введите новое описание для {widget.get(selection[0])}",
        bg="#DB22BD",
        fg="#fff",
    )
    desc_info.grid(row=1, column=1, pady=10)

    desc_entry = Entry(
        frame,
        background="#7E67E9",
        foreground="#fff"
    )
    desc_entry.grid(row=2, column=1, padx=15)

    image_button = Button(
        frame,
        text="Обновить картинку",
    )
    image_button.grid(row=2, column=2)

    user_button = Button(
        frame,
        text=f"Обновить {widget.get(selection[0])}",
    )
    user_button.grid(row=3, column=2, pady=10)

    user_button.bind('<Button-1>', lambda event: edit([fio_entry.get(), desc_entry.get(), widget.get(selection[0])], window))
    image_button.bind('<Button-1>', lambda event: edit_img(widget.get(selection[0]), window))


def edit_img(data, window):
    filename = filedialog.askopenfilename(title="Выбрать фотографию", initialdir="/", filetypes=[
        ('PNG pictures', '*.png'),
    ])
    if filename:
        database = DataBase("update personalities set image = ? where fio = ?")
        database.edit_image([filename, data])
    showinfo(title="Информация",
             message="Картинка успешно изменена")
    window.destroy()


def edit(data, window):
    print("data: ", data)
    if data[0] == "" and data[1] == "":
        showinfo(title="Памятка",
                 message="Данные не были изменены")
        window.destroy()
        return
    if data[0] != "" and data[1] != "":
        database = DataBase("update personalities set fio = ?, info = ? where fio = ?")
        database.exec([data[0], data[1], data[2]])
        showinfo(title="Памятка",
                 message="Данные успешно изменены")
        window.destroy()
        return
    if data[0] == "":
        database = DataBase("update personalities set info = ? where fio = ?")
        database.exec([data[1], data[2]])
        showinfo(title="Памятка",
                 message="Данные успешно изменены")
        window.destroy()
        return
    else:
        database = DataBase("update personalities set fio = ? where fio = ?")
        database.exec([data[0], data[2]])
        showinfo(title="Памятка",
                 message="Данные успешно изменены")
        window.destroy()
        return
