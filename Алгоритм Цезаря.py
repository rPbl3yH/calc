from tkinter import *
alfavit = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
root = Tk()
s1 = ''
def cifer():
    global s1
    s1.replace(s1,'')
    s2 = str(ent.get())
    for i in range(0,len(s2)):
        if s2[i] == alfavit[-1]:
            s1 += alfavit[0]
        else:
            for g in range(0,len(alfavit)):
                if s2[i] == alfavit[g]:
                    s1 += alfavit[g+1]
    ext2['text'] = s1
ext = Label(text = 'Введите слово для шифрования/дешифрования')
ent = Entry()
ext2 = Label()
btn = Button(text = 'Расшифровать!',command = cifer)
ext.pack()
ent.pack()
ext2.pack()
btn.pack()
#ent2 = Entry()
#ent2.pack()
root.mainloop()
