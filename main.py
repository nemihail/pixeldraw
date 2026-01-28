
import tkinter as tk

# Размеры окна в пикселях
rows = 500
cols = 500

# Создание главного окна приложения
root = tk.Tk()
root.title('Pixeldraw')  # Заголовок окна
root.geometry(f'{rows}x{cols}')  # Установка размеров окна
root.resizable(width=False, height=False)  # Запрет изменения размера окна

# Список доступных цветов для кнопок
colors = ['white', 'black']

# Функция-обработчик для изменения цвета при нажатии
def chcolor(event):
    """Меняет цвет кнопки на белый при клике левой кнопкой мыши"""
    cell = event.widget  # Получаем виджет, на котором произошло событие
    cell.configure(bg='white')  # Устанавливаем белый фон

# Настройка строк и столбцов для равномерного распределения
for r in range(10): 
    root.rowconfigure(index=r, weight=1)  # Все строки имеют одинаковый вес
for c in range(10): 
    root.columnconfigure(index=c, weight=1)  # Все столбцы имеют одинаковый вес

# Создание сетки 10x10 из кнопок
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

# Запуск главного цикла обработки событий
root.mainloop()
