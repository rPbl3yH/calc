from tkinter import *
root = Tk()
def cifer_one():
    global s1
    s1 = ''
    s1 = list(ent.get().lower())
    for i in range(0,len(s1)):
        for j in range(97,123):
            if j == 122:
                s1[i] = chr(97)
            elif ord(s1[i]) == j:
                s1[i] = chr(j+1)
                break
    ext2['text'] = ''.join(s1)
def cifer_two():
    global s2
    s2 = ''
    s2 = list(ent2.get().lower())
    for h in range(0,len(s2)):
        for g in range(97,123):
            if g == 97:
                s2[h] = chr(122)
            elif ord(s2[h]) == g:
                s2[h] = chr(g-1)
                break
    ext4['text'] = ''.join(s2)
ext = Label(text = 'Введите слово для шифрования')
ent = Entry()
ext2 = Label()
btn = Button(text = 'Расшифровать!',command = cifer_one)
ext.pack()
ent.pack()
ext2.pack()
btn.pack()
ext3 = Label(text = 'Введите слово для дешифрования')
ent2 = Entry()
ext4 = Label()
btn2 = Button(text = 'Расшифровать!',command = cifer_two)
ext3.pack()
ent2.pack()
ext4.pack()
btn2.pack()
root.mainloop()
