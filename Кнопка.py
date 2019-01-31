from tkinter import *
def button_clicked():
    print('Привет')
def clicker():
    global i
    i = i + 1
    button3['text'] = i
i = 0
root = Tk()
button1 = Button()
button1.pack()
button2 = Button(root, bg='red', text='Hello',command=button_clicked)
button2.pack()
button3 = Button(root, bg='green',command=clicker)
button3.pack()
root.mainloop()
