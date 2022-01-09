import random
a = []
b = []
tablitsa = []
tablitsa_itog = []
str1 = ""
str2 = "456789123"
str3 = "789123456"
str5 = "567891234"
str4 = "234567891"
str6 = "891234567"
str7 = "345678912"
str8 = "678912345"
str9 = "912345678"
table1 = []
table2 = []
table3 = []
table4 = []
table5 = []
table6  = []
table7 = []
table8 = []
table9 = []
number = 0
temp = []
n = 9
temp = []
temp_index_i = []
temp_index_j = []
vvod_i = 0
for i in range (1, 10):
    b.append(i)
for i in range (9):
    a.append([0]*9)
for j in range (len(a)):
    for i in range (len(a[j])):
        a[j][i] = b[i]
str1 = ''.join(str(e) for e in b)
for i in range (9):
    tablitsa.append([0]*9)
table1 = list(str1)
table2 = list(str2)
table3 = list(str3)
table4 = list(str4)
table5 = list(str5)
table6 = list(str6)
table7 = list(str7)
table8 = list(str8)
table9 = list(str9)
tablitsa = [table1, table2, table3, table4, table5, table6, table7, table8, table9]
number = random.randint(1,10)
perestanovki = random.randint(10,20)
for y in range (perestanovki):
    type_of_perestanovka = random.randint(1,3)
    if type_of_perestanovka == 1:

        j1 = random.randint(1,7)
        choice = random.randint(1,2)
        if choice == 1:
            j2 = j1+1
        else:
            j2 = j1-1
        for i in range (n):
            tablitsa[i][j1], tablitsa[i][j2] = tablitsa[i][j2], tablitsa[i][j1]
    elif type_of_perestanovka == 2:

        for i in range(len(tablitsa)):
            for j in range(i + 1, len(tablitsa[i])):
                tablitsa[i][j], tablitsa[j][i] = tablitsa[j][i], tablitsa[i][j]
    elif type_of_perestanovka == 3:

        i1 = random.randint(1,7)
        choice = random.randint(1,2)
        if choice == 1:
            i2 = i1+1
        else:
            i2 = i1-1
        for i in range (n):
            for j in range (len(tablitsa)):
                tablitsa[i1][j], tablitsa[i2][j] = tablitsa[i2][j], tablitsa[i1][j]

tablitsa_itog = tablitsa.copy()

for i in tablitsa:
    print(*i)
print()

for i in range(40):
    deleter_i = random.randint(1,7)
    deleter_j = random.randint(1,7)
    tablitsa_itog[deleter_i][deleter_j] = "*"

for i in tablitsa_itog:
    print(*i)
print("ха")
for i in tablitsa:
    print(*i)
for i in range (len(tablitsa_itog)):
    str1_1 =  tablitsa_itog[0]
    str1_2 = tablitsa_itog[1]
    str1_3 = tablitsa_itog[2]
    str1_4 = tablitsa_itog[3]
    str1_5 = tablitsa_itog[4]
    str1_6 = tablitsa_itog[5]
    str1_7 =  tablitsa_itog[6]
    str1_8 = tablitsa_itog[7]
    str1_9 = tablitsa_itog[8]



from tkinter import *

def click_button():
    global vvod_i
    vvod_i = 0
    print(vvod_i)
    return vvod_i
def click_button2():
    global vvod_i
    vvod_i = 1
    print(vvod_i)
    return vvod_i
def click_button3():
    global vvod_i
    vvod_i = 2
    print(vvod_i)
    return vvod_i
def click_button4():
    global vvod_i
    vvod_i = 3
    print(vvod_i)
    return vvod_i
def click_button5():
    global vvod_i
    vvod_i = 4
    print(vvod_i)
    return vvod_i
def click_button6():
    global vvod_i
    vvod_i = 5
    print(vvod_i)
    return vvod_i
def click_button7():
    global vvod_i
    vvod_i = 6
    print(vvod_i)
    return vvod_i
def click_button8():
    global vvod_i
    vvod_i = 7
    print(vvod_i)
    return vvod_i
def click_button9():
    global vvod_i
    vvod_i = 8
    print(vvod_i)
    return vvod_i




def click_button10():
    global vvod_j
    vvod_j = 0
    print(vvod_j)
    return vvod_j

def click_button11():
    global vvod_j
    vvod_j = 1
    print(vvod_j)
    return vvod_j

def click_button12():
    global vvod_j
    vvod_j = 2
    print(vvod_j)
    return vvod_j
def click_button13():
    global vvod_j
    vvod_j = 3
    print(vvod_j)
    return vvod_j
def click_button14():
    global vvod_j
    vvod_j = 4
    print(vvod_j)
    return vvod_j
def click_button15():
    global vvod_j
    vvod_j = 5
    print(vvod_j)
    return vvod_j
def click_button16():
    global vvod_j
    vvod_j = 6
    print(vvod_j)
    return vvod_j
def click_button17():
    global vvod_j
    vvod_j = 7
    print(vvod_j)
    return vvod_j
def click_button18():
    global vvod_j
    vvod_j = 8
    print(vvod_j)
    return vvod_j

def click_buttonv1():
    global vvod
    vvod = 1
    print(vvod)
def click_buttonv2():
    global vvod
    vvod = 2
    print(vvod)
def click_buttonv3():
    global vvod
    vvod = 3
    print(vvod)
def click_buttonv4():
    global vvod
    vvod = 4
    print(vvod)
def click_buttonv5():
    global vvod
    vvod = 5
    print(vvod)
def click_buttonv6():
    global vvod
    vvod = 6
    print(vvod)
def click_buttonv7():
    global vvod
    vvod = 7
    print(vvod)
def click_buttonv8():
    global vvod
    vvod = 8
    print(vvod)
def click_buttonv9():
    global vvod
    vvod = 9
    print(vvod)


def result():
    # print(vvod_i)
    # print(vvod_j)
    # print(vvod)
    print("Было:P",tablitsa[vvod_i][vvod_j])
    if tablitsa[vvod_i][vvod_j] == vvod:
        print("yes")
    if tablitsa[vvod_i][vvod_j] != vvod:
        print("no")

from tkinter import *

root = Tk()

root.geometry('700x600')
root.resizable(False, False)

c = Canvas(root, width=700, height=700, bg="#B5DAFE")
c.grid(row = 1, rowspan = 12, column = 3)
btn = Button(root, text="1", background="#DA70D6", foreground="black",
             padx="5", pady="5", font="16", command=click_button)
btn2 = Button(root, text="2", background="#DA70D6", foreground="black",
             padx="5", pady="5", font="16", command=click_button2)
btn3 = Button(root, text="3", background="#DA70D6", foreground="black",
             padx="5", pady="5", font="16", command=click_button3)
btn4 = Button(root,text="4", background="#DA70D6", foreground="black",
             padx="5", pady="5", font="16", command=click_button4)
btn5 = Button(root,text="5", background="#DA70D6", foreground="black",
             padx="5", pady="5", font="16", command=click_button5)
btn6 = Button(root,text="6", background="#DA70D6", foreground="black",
             padx="5", pady="5", font="16", command=click_button6)
btn7 = Button(root,text="7", background="#DA70D6", foreground="black",
             padx="5", pady="5", font="16", command=click_button7)
btn8 = Button(root,text="8", background="#DA70D6", foreground="black",
             padx="5", pady="5", font="16", command=click_button8)
btn9 = Button(root,text="9", background="#DA70D6", foreground="black",
             padx="5", pady="5", font="16", command=click_button9)
btn10 = Button(root, text="1", background="#FFCC00", foreground="black",
             padx="5", pady="5", font="16", command=click_button10)
btn11 = Button(root, text="2", background="#FFCC00", foreground="black",
             padx="5", pady="5", font="16", command=click_button11)
btn12 = Button(root, text="3", background="#FFCC00", foreground="black",
             padx="5", pady="5", font="16", command=click_button12)
btn13 = Button(root,text="4", background="#FFCC00", foreground="black",
             padx="5", pady="5", font="16", command=click_button13)
btn14 = Button(root,text="5", background="#FFCC00", foreground="black",
             padx="5", pady="5", font="16", command=click_button14)
btn15 = Button(root,text="6", background="#FFCC00", foreground="black",
             padx="5", pady="5", font="16", command=click_button15)
btn16 = Button(root,text="7", background="#FFCC00", foreground="black",
             padx="5", pady="5", font="16", command=click_button16)
btn17 = Button(root,text="8", background="#FFCC00", foreground="black",
             padx="5", pady="5", font="16", command=click_button17)
btn18 = Button(root,text="9", background="#FFCC00", foreground="black",
             padx="5", pady="5", font="16", command=click_button18)
btnv1 = Button(root,text="1", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=click_buttonv1)
btnv2 = Button(root,text="2", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=click_buttonv2)
btnv3 = Button(root,text="3", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=click_buttonv3)
btnv4 = Button(root,text="4", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=click_buttonv4)
btnv5 = Button(root,text="5", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=click_buttonv5)
btnv6 = Button(root,text="6", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=click_buttonv6)
btnv7 = Button(root,text="7", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=click_buttonv7)
btnv8 = Button(root,text="8", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=click_buttonv8)
btnv9 = Button(root,text="9", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=click_buttonv9)
btnres = Button(root,text="Проверить", background="#669900", foreground="black",
             padx="5", pady="5", font="16", command=result )


c.create_text(280, 50, text = str1_1, font="64")
c.create_text(280, 70, text = str1_2, font="64")
c.create_text(280, 90, text = str1_3, font="64")
c.create_text(280, 110, text = str1_4, font="64")
c.create_text(280, 130, text = str1_5, font="64")
c.create_text(280, 150, text = str1_6, font="64")
c.create_text(280, 170, text = str1_7, font="64")
c.create_text(280, 300, text = "Розовые кнопки - номер строки, желтые - номер столбца", font="64")
c.create_text(280, 320, text = "Зеленые - выбранное число (ответ)", font="64")
btn.grid()
btn.grid(row = 1, column = 0)
btn2.grid()
btn2.grid(row = 2, column = 0)
btn3.grid()
btn3.grid(row = 3, column = 0)
btn4.grid()
btn4.grid(row = 4, column = 0)
btn5.grid()
btn5.grid(row = 5, column = 0)
btn6.grid()
btn6.grid(row = 6, column = 0)
btn7.grid()
btn7.grid(row = 7, column = 0)
btn8.grid()
btn8.grid(row = 8, column = 0)
btn9.grid()
btn9.grid(row = 9, column = 0)

btn10.grid()
btn10.grid(row = 1, column = 1)
btn11.grid()
btn11.grid(row = 2, column = 1)
btn12.grid()
btn12.grid(row = 3, column = 1)
btn13.grid()
btn13.grid(row = 4, column = 1)
btn14.grid()
btn14.grid(row = 5, column = 1)
btn15.grid()
btn15.grid(row = 6, column = 1)
btn16.grid()
btn16.grid(row = 7, column = 1)
btn17.grid()
btn17.grid(row = 8, column = 1)
btn18.grid()
btn18.grid(row = 9, column = 1)

btnv1.grid()
btnv1.grid(row = 1, column = 2)
btnv2.grid()
btnv2.grid(row = 2, column = 2)
btnv3.grid()
btnv3.grid(row = 3, column = 2)
btnv4.grid()
btnv4.grid(row = 4, column = 2)
btnv5.grid()
btnv5.grid(row = 5, column = 2)
btnv6.grid()
btnv6.grid(row = 6, column = 2)
btnv7.grid()
btnv7.grid(row = 7, column = 2)
btnv8.grid()
btnv8.grid(row = 8, column = 2)
btnv9.grid()
btnv9.grid(row = 9, column = 2)
btnres.grid()
btnres.grid(row = 9, column = 3)



root.mainloop()
