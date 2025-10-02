from PIL import Image
import os

#target resolution
target_width,target_height = 500, 500

path = './Image_Editing/imgs'
pathout = './Image_Editing/editedImgs'

for file in os.listdir(path):
    # open file and prepare clean name for save
    image = Image.open(f'{path}/{file}')
    clean_name = os.path.splitext(file)[0]
    crop_img = image
    print(file)

    # checks image ratio and crops image to square
    if image.width > image.height:
        print('wide image')
        crop_factor = (image.width - image.height) /2
        crop_img = image.crop((crop_factor,0,image.width - crop_factor,image.height))
    elif image.width < image.height:
        print('tall image')
        crop_factor = (image.height - image.width) /2
        crop_img = image.crop((0,crop_factor,image.width ,image.height - crop_factor))
    else:
        print("square image")
        
    # resize and set all images to RGB
    edit = crop_img.resize((target_width, target_height)).convert("RGB")
    edit.save(f'{pathout}/{clean_name}_edit.jpg')
