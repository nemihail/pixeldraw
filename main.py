
# Конечно! Вот Ваш код на Python.

import tkinter as tk

rows = 500
cols = 500

root = tk.Tk()
root.title('Pixeldraw')
root.geometry(f'{rows}x{cols}')
root.resizable(width=False, height=False)

colors = ['white', 'black']

def chcolor(event):
    cell = event.widget
    cell.configure(bg='white')

var = tk.IntVar

for r in range(10): root.rowconfigure(index=r, weight=1)
for c in range(10): root.columnconfigure(index=c, weight=1)

for row in range(10):
    for col in range(10):
        cell = tk.Button(text=f'{row}, {col}', bg='black')
        cell.bind("<Button-1>", chcolor)
        cell.grid(row=row, column=col, ipadx=0, ipady=0, padx=0, pady=0, sticky='nsew')

root.mainloop()
