from zipfile import ZipFile

with ZipFile("C:/Users/tya/Downloads/Visual-C-Runtimes-All-in-One-May-2023.zip", "r") as zip:
    zip.extractall()
    
print(zip.namelist())