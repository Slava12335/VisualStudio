import random
from tkinter import *

def setwindom(root):
    root.title("Программа")
    root.resizable(False, False)
    width = 800
    height = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenwidth()
    x = int(ws / 2 - width / 2)
    y = int(wh / 2 - height / 2)
    root.geometry("{0}x{1}+{2}+{3}". format(width, height, x, y ))

root = Tk()
setwindom(root)

# Задание 1
#ggg = Listbox(root, font='TimesNewRoman 25')
#ra = []
#while True:
#    ffg = input("Введите 0 что вывести города. Введите название города:")
#    if ffg == '0':
#        print(ra)
#        for i in ra:
#            ggg.insert(END, i)
#        ggg.pack()
#        root.mainloop()
#        break
#    ra.append(ffg)

# Задание 6
#label = Label(root, text="None")
#button = Button(root, text = "Сгенерировать случайное число",font= "TimesNewRoman 15", bg= "red", fg= "white", command=lambda: label.config(text=random.randint(0, 100)))
#button.pack()
#label.pack()

# Задание 3
#label1 = Label(root, text = "центр вверх",font= "Tahoma 20", bg= "red", width=10, height=2)
#label1.pack(side='top')
#label2 = Label(root, text = "слева",font= "Tahoma 20", bg= "red", width=10, height=2)
#label2.pack(side='left')
#label3 = Label(root, text = "справа",font= "Tahoma 20", bg= "red", width=10, height=2)
#label3.pack(side='right')
#label4 = Label(root, text = "центр вниз",font= "Tahoma 20", bg= "red", width=10, height=2)
#label4.pack(side='bottom')

# Задание 4
#label1 = Label(root, text = "центр вверх",font= "Tahoma 20", bg= "red", width=10, height=2)
#label1.grid(padx=170, row=0, column=1, pady=0)
#label2 = Label(root, text = "слева",font= "Tahoma 20", bg= "pink", width=10, height=2)
#label2.grid(column=0)
#label3 = Label(root, text = "справа",font= "Tahoma 20", bg= "blue", width=10, height=2)
#label3.grid(column=2)
#label4 = Label(root, text = "центр вниз",font= "Tahoma 20", bg= "pink", width=10, height=2)
#label4.grid(column=1, pady=310)

# Задание 5
#r1 = input("Введите путь к картинке: ")
#r2 = float(input("Укажите масштаб изображения: "))
#photo = PhotoImage(file=r1)
#if r2 < 1.0:
#    photo = photo.subsample(int(1 / r2), int(1 / r2))
#if r2 > 1.0:
#    photo = photo.zoom(int(r2), int(r2))
#uu = Label(root, image=photo)
#uu.place(y=0, x=0, relwidth=1, relheigh=1)

# Задание 2
#frame = Frame(root)
#frame.pack()
#label11 = Label(root, text="Важная форма", font="Tahoma 20")
#label11.pack()
#text = Text(root, bd=2, font="TimesNewRoman", fg='black', width=85, height=10)
#text.pack(side="top")
#text2 = Text(root, bd=2, font="TimesNewRoman", fg='black', width=85, height=10)
#text2.pack(side="top")
#button = Button(root, text = "Отправить форму", font= "Tahoma 20")
#button.pack()

# Задание 7



root.mainloop()