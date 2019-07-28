import os

# Create new project directories
# Project source directory
project_name = input("Enter the name of the project: ")
path = "C:\\Users\\rnedl\\Desktop\\myprojects\\Python\\" + project_name

try:
    os.makedirs(path)
except OSError:
    print("Error trying to create the directory")
else:
    print("Directory created successfully.")

# Tests and Docs directories
try:
    os.makedirs(path + "\\tests")
    os.makedirs(path + "\\docs")
except OSError:
    print("Error trying to create the directory")
else:
    print("Directory created successfully.")

# Create license, readme, and requirements files
try:
    filepath = os.path.join(path, "README.md")    
    f = open(filepath, "w")
    f.close()
    filepath = os.path.join(path, "LICENSE")    
    f = open(filepath, "w")
    f.close()
    filepath = os.path.join(path, "requirements.txt")    
    f = open(filepath, "w")
    f.close()


except OSError:
    print("Error trying to create the files")
else:
    print("Files created successfully.")









    