# Reading files (.txt, .json, .csv)

############ CASE 1 (.txt file)
# file_path = "fileHandling/employee.txt"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print("File read successfully")
#         print(content)
# except FileNotFoundError:
#     print("File doesn't exist")
# except PermissionError:
#     print("You do not have permission to read that file")

############ CASE 1 (.json file)
# import json

# file_path = "fileHandling/employee.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print("File read successfully")
#         print(content)
# except FileNotFoundError:
#     print("File doesn't exist")
# except PermissionError:
#     print("You do not have permission to read that file")

############ CASE 1 (.json file)
import csv

file_path = "fileHandling/employee.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
        print("File read successfully")
        
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("You do not have permission to read that file")