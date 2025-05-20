from tkinter import *
from tkinter import ttk

def hello_button_handler() -> None:
    frase_label.config(text='Привет')

def bye_button_handler() -> None:
    frase_label.config(text='До свидания')

main_win = Tk()
main_win.title('homework 4.1 - switchers')
main_win.geometry('300x200')

frase_frame = ttk.Frame(main_win)

frase_label = ttk.Label(frase_frame, text="")
frase_label.pack(pady=20)

frase_frame.pack(fill="both", padx=10, pady=10)

buttons_frame = ttk.Frame(frase_frame)

hello_button = ttk.Button(buttons_frame, text="Привет", command=hello_button_handler)
bye_button = ttk.Button(buttons_frame, text="До свидания", command=bye_button_handler)

hello_button.pack(side="left", padx=5)
bye_button.pack(side="right", padx=5)

buttons_frame.pack()

main_win.mainloop()