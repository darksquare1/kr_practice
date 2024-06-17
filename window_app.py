from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys
from kr_generator import KrGenerator


def info():
    messagebox.showinfo('Информация',
                        'Привет, эта программа нужна для генерации первой контрольной по комплану для отработки своих навыков.\n'
                        'Прежде чем генерировать, убедись, что miktex добавлен в переменные среды path и установлен перечень необходимых пакетов.')


def packages(root):
    def inner():
        packages = [r'\usepackage[T2A]{fontenc}', r'\usepackage[utf8]{inputenc}',
                    r'\usepackage[english,russian]{babel}',
                    r'\usepackage{amsmath}', r'\usepackage{titlesec}', r'\usepackage{titling}',
                    r'\usepackage{geometry}', r'\usepackage{stix}']
        package_text = '\n'.join(packages)
        root.clipboard_clear()
        root.clipboard_append(package_text)
        messagebox.showinfo('Необходимые пакеты', f'{package_text}\n\nСкопировано в буфер обмена!')

    return inner


def generate():
    try:
        KrGenerator('files/template.tex')()
        pdf_path = os.path.abspath('files/kr.pdf')
        if getattr(sys, 'frozen', False):
            pdf_path = os.path.join(sys._MEIPASS, 'files', 'kr.pdf')
        messagebox.showinfo('Успех', 'Контрольная работа успешно сгенерирована!')
        webbrowser.open_new(r'file:///' + pdf_path.replace('\\', '/'))
    except Exception as e:
        messagebox.showerror('Ошибка', f'Произошла ошибка при генерации контрольной работы: {str(e)}')


def create_window():
    root = Tk()
    root.title('Тренировка по первой контрольной работе по ТФКП')

    window_width = 1200
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    label = Label(root, text='Тренировка по первой контрольной работе по ТФКП', fg='red', font=('Arial', 20))
    label.pack(pady=20)

    button_style = {
        'font': ('Arial', 14),
        'bg': '#4CAF50',
        'fg': 'white',
        'relief': 'raised',
        'bd': 3,
        'width': 20,
        'height': 2
    }

    btn1 = Button(root, text='Прочти!', command=info, **button_style)
    btn1.pack(pady=10)

    btn2 = Button(root, text='Перечень пакетов', command=packages(root), **button_style)
    btn2.pack(pady=20)

    btn3 = Button(root, text='Генерировать', command=generate, **button_style)
    btn3.pack(pady=30)

    root.mainloop()


if __name__ == '__main__':
    create_window()
