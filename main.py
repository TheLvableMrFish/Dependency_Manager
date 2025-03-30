import tkinter as tk
from tkinter import ttk
import csv
import os

def create_dependency(name, path, data):
    try:
        # Make sure path exists
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Make sure file doesn't exist
        if os.path.exists(path):
            return
        
        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print(f"CSV file created as : {path} for {name}")
    
    except Exception as e:
        print(f"Error creating {name} CSV file: {e}")

path = "temp"

# window
window = tk.Tk()
window.title('Dependency Manager')
window.geometry('600x400')

# run
window.mainloop()