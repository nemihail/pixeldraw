
"""
Конечно! Вот ваш код на Python,
который позволяет пользователю рисовать по клеточкам.
"""

import tkinter as tk # Graphical user interfce
from time import time # Замер function work time

# Window dimensions, pixels
rows = 500
cols = 500

# Main window parameters
root = tk.Tk()
root.title('Pixeldraw')
root.geometry(f'{rows}x{cols}')
root.resizable(width=False, height=False)


def timecounter(func):
    """Decorator, замеряющий function work time"""
    def wrapper(*args, **kwargs):
        if func.__name__ == 'generate':
            start_time = time()
            func(*args, **kwargs)
            print(f'Generation took {time() - start_time} seconds.')
        else:
            start_time = time()
            func(*args, **kwargs)
            print(f'Function worked for {time() - start_time} seconds.')
    return wrapper


def chcolor(event):
    """Change btn color to opposite after pressing it."""
    cell = event.widget
    cell.configure(bg='white') if cell['bg'] == 'black' else cell.configure(bg='black')


# Cells configurations
for r in range(10): root.rowconfigure(index=r, weight=1)
for c in range(10): root.columnconfigure(index=c, weight=1)


@timecounter
def generate():
    """Generate each of buttons on the window"""
    for row in range(10):
        for col in range(10):
            # Button with black BG
            cell = tk.Button(text=f'{row}, {col}', bg='black')
            
            # Left mouse pressed > chcolor function
            cell.bind("<Button-1>", chcolor)
            
            # Button place i the grid
            cell.grid( # Мне лень переводить это всё tbh
                row=row,          # Позиция в строке
                column=col,       # Позиция в столбце
                ipadx=0,          # Внутренний отступ по горизонтали
                ipady=0,          # Внутренний отступ по вертикали
                padx=0,           # Внешний отступ по горизонтали
                pady=0,           # Внешний отступ по вертикали
                sticky='nsew'     # Растягивание во всех направлениях
            ) 


generate()

# Main loop... Absolutely NOT obviously
root.mainloop()
