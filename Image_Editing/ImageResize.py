from PIL import Image
import os

target_width = 500
target_height = 500

path = './Image_Editing/imgs'
pathout = './Image_Editing/editedImgs'

print(os.listdir(path))

for file in os.listdir(path):
    image = Image.open(f'{path}/{file}')
    edit = image.resize((target_width, target_height))
    clean_name = os.path.splitext(file)[0]
    edit.save(f'{pathout}/{clean_name}_edit.jpg')
