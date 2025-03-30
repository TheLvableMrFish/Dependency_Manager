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

# Name Entry
name_label = ttk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_entry = ttk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Generate Dependency Button
dependency_btn = ttk.Button(window, text="Create", command=generate_csv)
dependency_btn.grid(row=0, column=2, columnspan=2, pady=5)

# run
window.mainloop()