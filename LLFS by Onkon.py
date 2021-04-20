from tkinter import *
from functools import partial

def validateLogin(name, book, date,section, id):
 print("Name entered : ", name.get())
 print("Book code entered : ", book.get())
 print("Date entered : ", date.get())
 print("Section entered : ", section.get())
 print("ID entered : ", id.get())

 return

#window
tkWindow = Tk()
tkWindow.geometry('550x250')
tkWindow.title('Fariaj Laibrary Submit Form')
tkWindow.configure(bg="#FFFACD")
tkWindow.resizable(False,False)

#name label and text entry box
nameLabel = Label(tkWindow, text="Name").grid(row=0, column=0)
name = StringVar()
nameEntry = Entry(tkWindow, textvariable=name).grid(row=0, column=1)

#book label and book entry box
bookLabel = Label(tkWindow,text="Book").grid(row=1, column=0)
book = StringVar()
bookEntry = Entry(tkWindow, textvariable=book,).grid(row=1, column=1)

#date label and date entry box
dateLabel = Label(tkWindow, text="Date").grid(row=2, column=0)
date = StringVar()
dateEntry = Entry(tkWindow, textvariable=date).grid(row=2, column=1)

#section label and section entry box
sectionLabel = Label(tkWindow, text="Section").grid(row=3, column=0)
section = StringVar()
sectionEntry = Entry(tkWindow, textvariable=section).grid(row=3, column=1)

#id label and id entry box
idLabel = Label(tkWindow, text="ID").grid(row=4, column=0)
id = StringVar()
idEntry = Entry(tkWindow, textvariable=id).grid(row=4, column=1)


validateLogin = partial(validateLogin, name, book, date, section, id )

#submit button
submitButton = Button(tkWindow, text="Submit",bg='#ffb3fe', command=validateLogin).grid(row=6, column=1)

tkWindow.mainloop()
