import os, re

path = './FileSystem/files'

print(os.listdir(path))
#os.rename('./FileSystem/files/file1.txt','./FileSystem/files/file_1.txt')

for file in os.listdir(path):
    number = re.findall("[0-9]+",file)[0]
    filetype = file.rsplit(".")[1]
    name = file.rsplit(number[0])[0]
    newfilepath = f'{path}/{name}_{number}.{filetype}'
    print(newfilepath)
    os.rename(f'{path}/{file}', newfilepath)

print(os.listdir(path))