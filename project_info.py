from tkinter.messagebox import showinfo

def openWindow(*args):
    showinfo(title="Памятка", message="База данных 'Знаменитые химики России' позволяет: добавлять/ изменять/ удалять информацию. "
                         "\n Клавиши программы: \n F1 - вызов справки о программе, "
                         "\n F2 - добавить в базу данных, \n "
                         "F3 - удалить из базы данных, "
                         "\n F4 - изменить запись в базе данных")
