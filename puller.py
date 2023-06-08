import tkinter as tk
from tkinter import filedialog, messagebox
import os

def execgitpull():
    for directory in directories:
        directory = directory.strip()  # Remove leading/trailing spaces
        os.chdir(directory)  # Change to the directory
        os.system('git pull')  # Execute 'git pull' command
# Function to add a directory to the array
def add_directory():
    directory = filedialog.askdirectory()
    if directory:
        directories.append(directory)
        update_listbox()

# Function to delete a directory from the array
def delete_directory():
    selected_indices = listbox.curselection()
    if selected_indices:
        for index in reversed(selected_indices):
            directories.pop(index)
        update_listbox()

# Function to update the listbox with the directories
def update_listbox():
    listbox.delete(0, tk.END)
    for directory in directories:
        listbox.insert(tk.END, directory)

# Function to save the directories to a file
def save_directories():
    with open(directory_file, "w") as file:
        file.write(",".join(directories))
    messagebox.showinfo("Directories Saved", "Directories have been saved to the file.")

# Create the main window
window = tk.Tk()
window.title("Directory Manager")

# Create a listbox to display the directories
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
listbox.pack(padx=10, pady=10)

# Create a button to add directories
add_button = tk.Button(window, text="Add Directory", command=add_directory)
add_button.pack(pady=5)

# Create a button to delete directories
delete_button = tk.Button(window, text="Delete Directory", command=delete_directory)
delete_button.pack(pady=5)

# Create a button to save the directories
save_button = tk.Button(window, text="Save Directories", command=save_directories)
save_button.pack(pady=5)

# Initialize the directories array
directories = []

# Read the directories from the file
directory_file = "listed-dir.txt"
with open(directory_file, "r") as file:
    directories = file.read().split(",")

# Update the listbox with the directories
update_listbox()

# Start the main loop
window.mainloop()
