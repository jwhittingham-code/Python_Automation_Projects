import os

path = './FileSystem/files'

print(os.listdir(path))
os.rename('./FileSystem/files/file1.txt','./FileSystem/files/file_1.txt')
print(os.listdir(path))