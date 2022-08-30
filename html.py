from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    db_name = 'database.db'

    def __init__(self,window):
        self.wind = window
        self.wind.title('Tabla de Contenido')

        #Create frame conainer
        frame = LabelFrame(self.wind, text='registre un Producto nuevo')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        #Name Input
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #Price Input
        Label(frame, text = 'price: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        #Button add Product
        ttk.Button(frame, text = 'Guardar producto', command = self.add_poduct).grid(row =3, columnspan = 2, sticky = W + E)
        # Output Messages
        self.message = Label(text = '' , fg = 'red' )
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text='Precio', anchor=CENTER)

        #Buttons
        ttk.Button(text = 'DElETE').grid(row = 5, column = 0, sticky = E + W)


        #filling the row
        self.get_products()


    def run_query(self,query, parametres = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametres)
            conn.commit()
        return result

    def get_products(self):
        #clean table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #query.data
        query = 'select * from product order by name desc'
        db_rows = self.run_query(query)
       


if __name__ == '__main__':
     window = Tk()
     Product(window)
     application = Product(window)
     window.mainloop()