directory_file = "listed-dir.txt"
directories = []

# Read the directories from the file
with open(directory_file, "r") as file:
    directory_list = file.read().split(",")

# Remove any leading/trailing white spaces from each directory
directories = [directory.strip() for directory in directory_list]

# Print the directories array
print(directories)
