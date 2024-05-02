
import os
from datetime import datetime

# Define the path for the new folder
folder_path = "C:/Space_Detect_Output"

# Check if the folder already exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Get file names with spaces
print("*** Welcome To File Name Space Detection App ***")
directory = input("Please Paste Source Path: ")

try:
    files = os.listdir(directory)
    # Create a text file to store the file names
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_names_file = os.path.join(folder_path, f"{current_time}.txt")

    # Write file names without extensions and with date and time to the text file
    with open(file_names_file, "w") as f:
        f.write("File Names with Spaces Details :\n")
        for file in files:
            if ' ' in file:
                file_name = os.path.splitext(file)[0]  
                f.write(file_name + "\n")
    print("File names with spaces saved to:", file_names_file)
except FileNotFoundError as e:
    print(f"Check the file path: {directory}")


