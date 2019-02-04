from tkinter import *
root = Tk()
def cifer():
    global s2
    s2 = ''
    s2 = list(ent.get().lower())
    for i in range(0,len(s2)):
        for j in range(97,123):
            if j == 122:
	            ord(s2[i]) = 97 
	    elif ord(s2[i]) == j:
            ord(s2[i]) = j+1
	        break 
    s2.join
    ext2['text'] = s2
ext = Label(text = 'Введите слово для шифрования/дешифрования')
ent = Entry()
ext2 = Label()
btn = Button(text = 'Расшифровать!',command = cifer)
ext.pack()
ent.pack()
ext2.pack()
btn.pack()
root.mainloop()
