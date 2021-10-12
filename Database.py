import mysql.connector
from tkinter import *


root = Tk()
root.title("Mysql Database")
root.resizable(False, False)
root.geometry("500x500+10+100")
#connect mysql..........
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="shamim123",
    database='Rock'
)

#create a cursor and initialize it...........
my_cursor = db.cursor()



#show record.................................................................................................
my_cursor.execute("SELECT * FROM tbb")
result = my_cursor.fetchall()
for i in result:
   print(i)

#Add Function................
def clear():
    name_ent.delete(0, END)
    roll_ent.delete(0, END)
    id_ent.delete(0, END)

def add():
    name = "INSERT INTO tbb (Name, Roll, ID) VALUES(%s,%s,%s)"
    values = (name_ent.get(),roll_ent.get(),id_ent.get())
    my_cursor.execute(name, values)

    db.commit()
    clear()


#Create tkinter Label................

label1 = Label(root, text="Name :")
label1.grid(row=0, column=0)

label2 = Label(root, text="Roll :")
label2.grid(row=1, column=0)

label3 = Label(root, text="ID :")
label3.grid(row=2, column=0)

#create input box.........

name_ent = Entry(root)
name_ent.place(x=50, y=0)

roll_ent = Entry(root)
roll_ent.place(x=50, y=20)

id_ent = Entry(root)
id_ent.place(x=50, y=40)


#Create butoon...........................
add_db_button = Button(root, text="Add all record", command=add)
add_db_button.grid(row=3, column=3, padx=20, pady=15)


#Create database...............
#my_cursor.execute("CREATE DATABASE Rock")

#Show database................................
#my_cursor.execute("show databases")
#for i in my_cursor:
    #print(i)


#create A table.............
#my_cursor.execute("CREATE TABLE tbb (Name VARCHAR(255), Roll VARCHAR(255), ID INT PRIMARY KEY)")


root.mainloop()