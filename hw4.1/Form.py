from tkinter import *
from tkinter import ttk

def submit() -> None:
    print(f'''
        name - {name_entry.get()}
        surname - {surname_entry.get()}
        email - {email_entry.get()}
    ''')

main_win = Tk()
main_win.geometry('600x400')
main_win.title('homework 4.1 - Form')

info_label = ttk.Label(main_win, text='Форма регистрации', font=('Aerial', 15))
info_label.place(x=200, y=20)

name_label = ttk.Label(main_win, text='Имя:', justify=CENTER)
name_entry = ttk.Entry(main_win)
name_label.place(x=280, y=90)
name_entry.place(x=245, y=120, width=100)

surname_label = ttk.Label(main_win, text='Фамилия:', justify=CENTER)
surname_entry = ttk.Entry(main_win)
surname_label.place(x=265, y=160)
surname_entry.place(x=245, y=190, width=100)

email_label = ttk.Label(main_win, text='E-mail:', justify=CENTER)
email_entry = ttk.Entry(main_win)
email_label.place(x=275, y=230)
email_entry.place(x=245, y=260, width=100)

submit_button = ttk.Button(main_win, text='Submit', command=submit)
submit_button.place(x=245, y=300, width=100, height=30)

main_win.mainloop()