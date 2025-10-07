import os, re

path = './FileSystem/files'

#Print list of current files
print("Current files: ", os.listdir(path))


for file in os.listdir(path):
    number = re.findall("[0-9]+",file)[0]
    filetype = file.rsplit(".")[1]
    name = file.rsplit(number[0])[0]
    newfilepath = f'{path}/{name}_{number}.{filetype}'
    
    os.rename(f'{path}/{file}', newfilepath)

print("Renamed files: ", os.listdir(path))