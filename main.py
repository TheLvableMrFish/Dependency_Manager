import tkinter as tk
from tkinter import ttk
import csv
import os

def create_dependency(name, path, fileData):
    try:
        # Make sure path exists
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Make sure file doesn't exist
        if os.path.exists(path):
            return
        
        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(fileData)
        print(f"CSV file created as : {path} for {name}")
    
    except Exception as e:
        print(f"Error creating {name} CSV file: {e}")

def generate_csv():
    name = name_entry.get()
    path = '' + name + ".csv"
    fileData = [
        ['header', 'start', 'works'],
        ['another', 'working', 'thing']
    ]
    create_dependency(name, path, fileData)

# Window
window = tk.Tk()
window.title('Dependency Manager')
window.geometry('600x400')
window.minsize(295,100)

notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
# tab2 = ttk.Frame(notebook)
# tab3 = ttk.Frame(notebook)

# Tab 1
notebook.add(tab1, text = 'Tab 1')
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
dependency_btn = ttk.Button(tab1, text="Create", command=generate_csv)
dependency_btn.grid(row=0, column=2, padx=10, pady=5, sticky='w')

notebook.pack(fill='both')

# run
window.mainloop()