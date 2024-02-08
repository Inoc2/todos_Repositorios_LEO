from tkinter import *
from tkinter.ttk import Combobox
#Modulo ttk do pacote tkinter
#Apresenta diferenciação de caixa

window = Tk()
def button_clicked(event):
    label_label_1.configure(text="Você clicou no botão!")
def double_button_clicked(event):
    label_label_1.configure(text="Você clicou 2 vezes no botão!")
# def user_pressed_letter_a():
#     label_label_1(window, text="Você pressionou a letra "a"!", command=click)

fonte = ("Helvetica", 16)
window.title("Teste")
window.geometry("300x300")

label_label_1 = Label(window, text="Olá")
label_label_1.pack()

botao = Button(window, text="Clique aqui")
botao.bind('<Button-1>', button_clicked)
botao.bind('<Double-Button-1>', double_button_clicked)
botao.pack()

label_label_2 = Label(window, text="Esta é uma janela label", fg="blue")
label_label_2.place(x = 90, y = 50)

text_bot_1 = Entry(window, text="Esta é uma janela vazia.", bd = 6)
text_bot_1.place(x = 80, y = 90)

data_ttk = "Um", "Dois", "Três", "Quatro", "Cinco"
combo_box_1 = Combobox(window, values=data_ttk)
combo_box_1.place(x = 75, y = 130)

list_box_1 = Listbox(window, height = 5, selectmode='multiple')
for numero in data_ttk:
    list_box_1.insert(END, numero)
list_box_1.place(x = 85, y = 160)

radio_button_v1 = IntVar()
radio_button_v1.set(1)
radio_button_v1_value_1 = Radiobutton(window, text='Programação', variable=radio_button_v1, value=1)
radio_button_v1_value_2 = Radiobutton(window, text='Infra', variable=radio_button_v1, value = 2)
radio_button_v1_value_1.place(x = 70, y = 240)
radio_button_v1_value_2.place(x = 170, y = 240)

window.mainloop()
