# Python file detection
# test.txt belongs
import os

# file_path1 = "fileHandling/test.txt"

# if os.path.exists(file_path1):
#     print(f"The location {file_path1} exists")
# else:
#     print("That location doesn't exist")


file_path2 = "G:/D DRIVE/Desktop/exists.txt"

if os.path.exists(file_path2):
    print(f"The location {file_path2} exists")
    if os.path.isfile(file_path2):
        print("That is a file")
    elif os.path.isdir(file_path2):
        print("That is a directory")
else:
    print("That location doesn't exist")
