from tkinter import *

root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x300")


btn = Button(text="Hello",          # текст кнопки
             background="red",     # фоновый цвет кнопки
             foreground="black",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16"              # высота шрифта
             )
btn.pack()


lbl = Label (text= "Label")
lbl.pack()
root.mainloop()