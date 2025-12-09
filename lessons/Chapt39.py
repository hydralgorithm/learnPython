# Python writing files (.txt, .json, .csv)

txt_data = "I like pizza! and I'm linked to Chapt39.py"
############ CASE 1 (.txt file)
# file_path = "fileHandling/output.txt"

# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")


############ CASE 2 (.txt file)
# file_path = "G:/D DRIVE/Desktop/alsoexists.txt"

# try:
#     with open(file_path, "x") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("File already exists and hence cannot be rewritten or recreated")

############ CASE 3 (.txt file)
# txt_data2 = ".\nLooks like it got appended as well with me :3"
# file_path = "fileHandling/output.txt"

# with open(file_path, "a") as file:
#     file.write(txt_data2)
#     print(f"txt file '{file_path}' was appended")

############ CASE 4 (.txt file)
# employess = ["Eugene","Squidward","Patrick","Sandy"]
# file_path = "fileHandling/employee.txt"

# try:
#     with open(file_path,"w") as file:
#         for employee in employess:
#             file.write(employee + "\n")
#         print(f"txt file {file_path} was created")
# except FileExistsError:
#     print("File already exists")

############ CASE 1 (.json file)
# import json

# employee = {
#     "name" : "Spongebob",
#     "age" : 30,
#     "job" : "cook"
# }

# file_path = "fileHandling/employee.json"

# try:
#     with open(file_path,"w") as file:
#         json.dump(employee, file, indent = 4)
#         print(f"json file {file_path} was created")
# except FileExistsError:
#      print("File already exists")

############ CASE 1 (.csv file)
import csv

employees = [["Name","Age","Job"],
             ["Jony",25,"Cashier"],
             ["Tim",19,"Manager"],
             ["Boba",30,"Cook"]]

file_path = "fileHandling/employee.csv"

try:
    with open(file_path,"w", newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
     print("File already exists")