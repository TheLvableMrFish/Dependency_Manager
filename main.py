import tkinter as tk
from tkinter import ttk

from functions import generate_csv

# Window
window = tk.Tk()
window.title('Dependency Manager')
window.geometry('600x400')
window.minsize(295,100)
window.maxsize(1920, 1080)

notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Tab 1
notebook.add(tab1, text = 'Generate Dependency')
# label_tab1 = ttk.Label(tab1, text='Text in tab 1')
# label_tab1.pack(side='top', anchor='w')
# button_tab1 = ttk.Button(tab1, text="Button in tab 1")
# button_tab1.pack(side='top', anchor='w')

# Name Entry
# name_label = ttk.Label(tab1, text="Name:")
# name_label.pack(padx='5', pady='5', side='left', anchor='w')
# name_entry = ttk.Entry(tab1)
# name_entry.pack(padx='5', pady='5', side='left', anchor='w')

# # Generate Dependency Button
# dependency_btn = ttk.Button(tab1, text="Create", command=generate_csv)
# dependency_btn.pack(padx='5', pady='5', side='left', anchor='w')

# Name Entry
name_label = ttk.Label(tab1, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_entry = ttk.Entry(tab1)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Generate Dependency Button
dependency_btn = ttk.Button(tab1, text="Create", command=lambda: generate_csv(name_entry.get()))
dependency_btn.grid(row=0, column=2, padx=10, pady=5, sticky='w')

# Tab 2
notebook.add(tab2, text = 'Edit Dependency')

# Name Entry
name_label2 = ttk.Label(tab2, text="Name:")
name_label2.grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_entry2 = ttk.Entry(tab2)
name_entry2.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Tab 3
notebook.add(tab3, text = 'Group Dependencies')

# Name Entry
name_label2 = ttk.Label(tab3, text="Name:")
name_label2.grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_entry2 = ttk.Entry(tab3)
name_entry2.grid(row=0, column=1, padx=10, pady=5, sticky='w')

notebook.pack(fill='both')

# run
window.mainloop()