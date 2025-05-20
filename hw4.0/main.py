from tkinter import *
from functions import *
from tkinter import ttk


def button_handler(func):
    def find():
        list_numbers: list[int] = [int(el) for el in entry_data.get().split(', ')]

        if (func == is_monotone):
            result_data_label.config(text=('да' if is_monotone(list_numbers) else 'нет'))
            return

        result: float = func(list_numbers)
        result_data_label.config(text=str(result))

    return find


main_win = Tk()
main_win.title('Homework 4.0')
main_win.geometry('600x400')

# --- LABELS --- #

info_label = ttk.Label(main_win, text='Введите список чисел через запятую')
info_label.place(x=47, y=50)

result_text_label = ttk.Label(main_win, text='результат:')
result_text_label.place(x=400, y=50)

result_data_label = ttk.Label(main_win, text='...')
result_data_label.place(x=425, y=70)

# --- ENTRIES --- #

entry_data = ttk.Entry(main_win)
entry_data.place(x=50, y=70, width=200)

find_min_element_button = ttk.Button(main_win, text='Найти минимальный элемент', command=button_handler(find_min))
find_min_element_button.place(x=20, y=120, width=260, height=40)

find_avg_button = ttk.Button(main_win, text='Найти среднее значение элементов', command=button_handler(find_avg))
find_avg_button.place(x=20, y=170, width=260, height=40)

find_second_max_element_button = ttk.Button(main_win, text='Найти второй максимум среди элементов', command=button_handler(find_second_max))
find_second_max_element_button.place(x=20, y=220, width=260, height=40)

find_sum_even_elements_button = ttk.Button(main_win, text='Найти сумму четных элементов', command=button_handler(find_sum_of_even_nums))
find_sum_even_elements_button.place(x=20, y=270, width=260, height=40)

is_monotone_button = ttk.Button(main_win, text='Это монотонный список?', command=button_handler(is_monotone))
is_monotone_button.place(x=20, y=320, width=260, height=40)

main_win.mainloop()