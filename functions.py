import csv
import os

def generate_csv(name):
    name = name
    path = '' + name + ".csv"
    fileData = [
        ['header', 'start', 'works'],
        ['another', 'working', 'thing']
    ]
    create_dependency(name, path, fileData)

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
