import os
file=os.mkdir("sample1.txt")
if 'file' in locals():
    print("directorry created successfully")
print(os.getcwd())
print(os.listdir())


path="sample1.txt"
if os.path.isfile(path):
    print(f"{path} is a file")
elif os.path.isdir(path):
    print(f"{path} is directory")
else:
    print(f"{path} is neither a file nor a directory")
    
absolute_path=os.path.abspath(path)
print(absolute_path)