from tkinter import *
root = Tk()
koper = 0
def ext1():
    global lbl_conclusion
    lbl_conclusion['text'] += '1'                        #Функция при нажатии кнопки 1
def ext2():
    global lbl_conclusion                               
    lbl_conclusion['text'] += '2'                        #Функция при нажатии кнопки 2
def ext3():
    global lbl_conclusion
    lbl_conclusion['text'] += '3'                       #Функция при нажатии кнопки 3
def ext4():
    global lbl_conclusion
    lbl_conclusion['text'] += '4'                      #Функция при нажатии кнопки 4
def ext5():
    global lbl_conclusion
    lbl_conclusion['text'] += '5'                      #Функция при нажатии кнопки 5 
def ext6():
    global lbl_conclusion
    lbl_conclusion['text'] += '6'                      #Функция при нажатии кнопки 6 
def ext7():
    global lbl_conclusion
    lbl_conclusion['text'] += '7'                       #Функция при нажатии кнопки 7
def ext8():
    global lbl_conclusion
    lbl_conclusion['text'] += '8'                       #Функция при нажатии кнопки 8
def ext9():
    global lbl_conclusion
    lbl_conclusion['text'] += '9'                       #Функция при нажатии кнопки 9
def ext0():
    global lbl_conclusion
    lbl_conclusion['text'] += '0'                       #Функция при нажатии кнопки 0
def oper_plus():
    global lbl_conclusion, koper, znach_1
    koper = 1
    znach_1 = int(lbl_conclusion['text'])
    lbl_conclusion['text'] = ''
def oper_minus():
    global lbl_conclusion, koper, znach_1
    koper = 2
    znach_1 = int(lbl_conclusion['text'])
    lbl_conclusion['text'] = ''
def oper_ymnog():
    global lbl_conclusion, koper, znach_1
    koper = 3
    znach_1 = int(lbl_conclusion['text'])
    lbl_conclusion['text'] = ''
def oper_del():
    global lbl_conclusion, koper, znach_1
    koper = 4
    znach_1 = int(lbl_conclusion['text'])
    lbl_conclusion['text'] = ''
def oper_ravno():
    global lbl_conclusion, znach_1, znach_2, koper
    znach_2 = int(lbl_conclusion['text'])
    lbl_conclusion['text'] = ''
    if koper == 1:
        rvn = znach_1 + znach_2
    elif koper == 2:
        rvn = znach_1 - znach_2
    elif koper == 3:
        rvn = znach_1 * znach_2
    elif koper == 4:
        rvn = znach_1 / znach_2
    lbl_conclusion['text'] = rvn
def oper_delete():
    global lbl_conclusion
    lbl_conclusion['text'] = ''
lbl_conclusion = Label(root, font = 'Arial 20', height = 2, width = 15)
btn_1 = Button(root, text = '1', font = 'Arial 18', height = 2, width = 5, command = ext1)
btn_2 = Button(root, text = '2', font = 'Arial 18', height = 2, width = 5, command = ext2)
btn_3 = Button(root, text = '3', font = 'Arial 18', height = 2, width = 5, command = ext3)
btn_4 = Button(root, text = '4', font = 'Arial 18', height = 2, width = 5, command = ext4)
btn_5 = Button(root, text = '5', font = 'Arial 18', height = 2, width = 5, command = ext5)
btn_6 = Button(root, text = '6', font = 'Arial 18', height = 2, width = 5, command = ext6)
btn_7 = Button(root, text = '7', font = 'Arial 18', height = 2, width = 5, command = ext7)
btn_8 = Button(root, text = '8', font = 'Arial 18', height = 2, width = 5, command = ext8)
btn_9 = Button(root, text = '9', font = 'Arial 18', height = 2, width = 5, command = ext9)
btn_0 = Button(root, text = '0', font = 'Arial 18', height = 2, width = 5, command = ext0)
btn_plus = Button(root, text = '+',font = 'Arial 18', height = 2, width = 5, command = oper_plus)
btn_minus = Button(root, text = '-', font = 'Arial 18', height = 2, width = 5, command = oper_minus)
btn_ymnog = Button(root, text = '*', font = 'Arial 18', height = 2, width = 5, command = oper_ymnog)
btn_del = Button(root, text = '/', font = 'Arial 18', height = 2, width = 5, command = oper_del)
btn_ravno = Button(root, text = '=', font = 'Arial 18', height = 2, width = 5, command = oper_ravno)
btn_delete = Button(root, text = 'Delete', font = 'Arial 18',height = 2,width = 5, command = oper_del)
btn_1.grid(row = 1, column = 0)
btn_2.grid(row = 1, column = 1)
btn_3.grid(row = 1, column = 2)
btn_4.grid(row = 2, column = 0)
btn_5.grid(row = 2, column = 1)
btn_6.grid(row = 2, column = 2)
btn_7.grid(row = 3, column = 0)
btn_8.grid(row = 3, column = 1)
btn_9.grid(row = 3, column = 2)
btn_0.grid(row = 4, column = 0)
btn_plus.grid(row = 1, column = 3)
btn_minus.grid(row = 2, column = 3)
btn_ymnog.grid(row = 3, column = 3)
btn_del.grid(row = 4, column = 3)
btn_ravno.grid(row = 4, column = 2)
btn_delete.grid(row = 4, column = 1)
lbl_conclusion.grid(row = 0, column = 0, columnspan = 4)
root.mainloop()
