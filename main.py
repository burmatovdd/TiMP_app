import add_new_user
import delete_user
import edit_user
import project_info
import config
import about_project
from db import DataBase
import os.path
from tkinter import *
from PIL import Image, ImageTk


class App:
    def __init__(self):
        print("project is starting...")

    def run(self):
        config.config = config.get_settings("config/config.ini")
        database = DataBase(None)
        if not exists("./"+config.config.get('Database', 'datasource')):
            database.createDB()
        else:
            print("database already exist")

        window = Tk()
        window.title("Знаменитые химики России")
        window["bg"] = "#1C1A3F"
        window.minsize(900, 450)

        main_menu = Menu(window)
        window.config(menu=main_menu)

        func_menu = Menu(window, tearoff=0)
        func_menu.add_command(label="Добавить нового химика: F2", command=add_new_user.openWindow)
        func_menu.add_command(label="Удалить химика: F3", command=delete_user.openWindow)
        func_menu.add_command(label="Изменить химика: F4", command=edit_user.openWindow)
        func_menu.add_separator()
        func_menu.add_command(label="Выйти из программы: crtl+x")
        main_menu.add_cascade(label="Основное", menu=func_menu)

        window.bind('<F2>', add_new_user.openWindow)
        window.bind('<F3>', delete_user.openWindow)
        window.bind('<F4>', edit_user.openWindow)
        window.bind('<F5>', lambda event: quit(window))

        info_menu = Menu(window, tearoff=0)
        info_menu.add_command(label="Памятка", command=project_info.openWindow)
        info_menu.add_command(label="О программе", command=about_project.openWindow)
        main_menu.add_cascade(label="Справка", menu=info_menu)

        list_frame = Frame(
            window,
            padx=10,
            pady=10,
            height=100,
            bg="#785BF4",
        )
        list_frame.pack(expand=True)

        refresh_button = Button(
            list_frame,
            bg="#785BF4",
            text="обновить",
            borderwidth=0,
        )
        refresh_button.grid(row=1, column=1)
        refresh_button.bind('<Button-1>', lambda event: self.refresh(window, list_frame))

        window.mainloop()

    def refresh(self, window, list_frame):

        chems = []
        database = DataBase("select * from personalities")
        data = database.select(None)
        chem_list = Listbox(
            list_frame,
            bg="#785BF4",
            fg="#fff",
            borderwidth=0,
            width=27
        )
        print("data: ", data)
        chem_list.grid(row=0, column=1, pady=(5, 0))
        chem_list.bind('<<ListboxSelect>>', self.on_change)

        self.canvas = Canvas(list_frame, width=200, height=200, highlightthickness=0)

        self.chem_info = Text(
            list_frame,
            bg="#221F4A",
            fg="#fff",
            wrap=WORD,
            width=27
        )
        self.chem_info.grid(row=0, column=3, padx=15)

        for item in data:
            print("item: ", item)
            chems.append(item[0])
            chem_list.insert(0, item[0])
            self.img = Image.open(item[2])
            self.img = self.img.resize((200, 200), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(0, 0, anchor='nw', image=self.image)
            self.canvas.grid(row=0, column=2)
        window.update()

    def on_change(self, event):
        widget = event.widget
        selection = widget.curselection()

        if selection:
            text = widget.get(selection[0])
            param = [text]
            conn = DataBase("Select * from personalities where fio = ?")
            data = conn.select(param)
            print(data)
            self.chem_info.delete("1.0", END)
            self.chem_info.insert("1.0", data[0][1])
            self.img = Image.open(data[0][2])
            self.img = self.img.resize((200, 200), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(0, 0, anchor='nw', image=self.image)
            self.canvas.grid(row=0, column=2)


def quit(window):
    print("poka...")
    window.quit()


def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True


if __name__ == "__main__":
    app = App()
    app.run()
