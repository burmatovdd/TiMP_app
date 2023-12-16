import sqlite3
from tkinter.messagebox import showerror
class DataBase:
    def __init__(self, query):
        self.query = query

    def createDB(self):
        try:
            connection = sqlite3.connect("AmDB.db")
            connection.execute(
                "CREATE TABLE personalities(id INTEGER PRIMARY KEY AUTOINCREMENT,  fio TEXT, info TEXT, image BLOB)")
            print("Successfully created new DB")
        except sqlite3.Error as err:
            showerror(title="Ошибка", message=f"Error connecting to sqlite: {err}")
        finally:
            if (connection):
                connection.close()
                print("The connection to SQLite is closed")

    def insert(self, params):
        try:
            print("params: ", params)
            connection = sqlite3.connect("AmDB.db")
            cursor = connection.cursor()
            print("Successfully connected to SQLite")

            with open(params[2], 'rb') as file:
                blobData = file.read()

            data_tuple = (params[0], params[1], blobData)
            cursor.execute(self.query, data_tuple)
            print("Image and file inserted successfully as a BLOB into a table")
            connection.commit()
            cursor.close()
        except sqlite3.Error as err:
            showerror(title="Ошибка", message=f"Error connecting to sqlite: {err}")
        finally:
            if (connection):
                connection.close()
                print("The connection to SQLite is closed")

    def writeTofile(self, photo, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(photo)

    def select(self, params):
        try:
            connection = sqlite3.connect("AmDB.db")
            cursor = connection.cursor()
            print("Successfully connected to SQLite")
            if params is None:
                cursor.execute(self.query)
            else:
                cursor.execute(self.query, (*params,))

            users = []

            record = cursor.fetchall()
            for row in record:
                print("Storing employee image on disk \n")
                imagePath = "./output-images/" + row[1] + ".png"
                self.writeTofile(row[3], imagePath)
                users.append([row[1], row[2], imagePath])

            cursor.close()

        except sqlite3.Error as err:
            showerror(title="Ошибка", message=f"Error connecting to sqlite: {err}")
        finally:
            if (connection):
                connection.close()
                print("The connection to SQLite is closed")
                return users

    def exec(self, params):
        try:
            connection = sqlite3.connect("AmDB.db")
            cursor = connection.cursor()
            print("Successfully connected to SQLite")
            cursor.execute(self.query, (*params,))
            connection.commit()
        except sqlite3.Error as err:
            showerror(title="Ошибка", message=f"Error connecting to sqlite: {err}")
        finally:
            if (connection):
                connection.close()
                print("The connection to SQLite is closed")

    def edit_image(self, params):
        try:
            print("params: ", params)
            connection = sqlite3.connect("AmDB.db")
            cursor = connection.cursor()
            print("Successfully connected to SQLite")
            with open(params[0], 'rb') as file:
                blobData = file.read()
            data_tuple = (blobData, params[1])
            cursor.execute(self.query, data_tuple)
            print("Image and file inserted successfully as a BLOB into a table")
            connection.commit()
            cursor.close()
        except sqlite3.Error as err:
            showerror(title="Ошибка", message=f"Error connecting to sqlite: {err}")
        finally:
            if (connection):
                connection.close()
                print("The connection to SQLite is closed")




