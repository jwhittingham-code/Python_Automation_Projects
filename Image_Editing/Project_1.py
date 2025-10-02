from PIL import Image, ImageEnhance, ImageFilter
import os

#Note that the . origin for a path is the top level project folder.
#Need to path correctly down to solve errors
path = './Image_Editing/imgs'
pathout = './Image_Editing/editedImgs'

print(os.listdir(path))

#This Loop takes all files in the img folder, sharpens and then saves them in the edited folder.
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathout}/{clean_name}_edited.jpg')