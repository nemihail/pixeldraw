
import tkinter as tk # Графический интерфейс
from time import time # Замер врмени работы функции

# Размеры окна в пикселях
rows = 500
cols = 500

# Создание главного окна приложения
root = tk.Tk()
root.title('Pixeldraw')  # Заголовок окна
root.geometry(f'{rows}x{cols}')  # Установка размеров окна
root.resizable(width=False, height=False)  # Запрет изменения размера окна


def timecounter(func):
    """Декторатор, замеряющий время выполнения функции"""
    def wrapper(*args, **kwargs):
        if func.__name__ == 'generate':
            start_time = time()
            func(*args, **kwargs)
            print(f'Генерация заняла {time() - start_time} секунд.')
        else:
            start_time = time()
            func(*args, **kwargs)
            print(f'Функция работала {time() - start_time} секунд.')
    return wrapper


# Функция-обработчик для изменения цвета при нажатии
def chcolor(event):
    """Меняет цвет кнопки на белый при клике левой кнопкой мыши"""
    cell = event.widget
    cell.configure(bg='white') if cell['bg'] == 'black' else cell.configure(bg='black')


# Конфигурация ячеек, в которых лежат кнопки
for r in range(10): root.rowconfigure(index=r, weight=1)
for c in range(10): root.columnconfigure(index=c, weight=1)


@timecounter
def generate():
    """Генерирует каждую из кнопок в окне"""
    for row in range(10):
        for col in range(10):
            # Создание кнопки с начальным черным фоном
            cell = tk.Button(text=f'{row}, {col}', bg='black')
            
            # Привязка функции chcolor к событию "клик левой кнопкой мыши"
            cell.bind("<Button-1>", chcolor)
            
            # Размещение кнопки в сетке с настройками отступов
            cell.grid(
                row=row,          # Позиция в строке
                column=col,       # Позиция в столбце
                ipadx=0,          # Внутренний отступ по горизонтали
                ipady=0,          # Внутренний отступ по вертикали
                padx=0,           # Внешний отступ по горизонтали
                pady=0,           # Внешний отступ по вертикали
                sticky='nsew'     # Растягивание во всех направлениях
            )


generate()

# Запуск главного цикла обработки событий
root.mainloop()
