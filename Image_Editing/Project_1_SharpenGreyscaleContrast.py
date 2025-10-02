from PIL import Image, ImageEnhance, ImageFilter
import os

#Note that the . origin for a path is the top level project folder.
#Need to path correctly down to solve errors
path = './Image_Editing/imgs'
pathout = './Image_Editing/editedImgs'

print(os.listdir(path))

# This Loop takes all files in the img folder, sharpens, converts to grescale and ups contrast.
# then saves them in the edited folder.
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    #convert L converts image to greyscale

    #this block increases contrast
    # we set a factor to increase by
    #then create the object to in ehance then enhance it by the factor value.
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathout}/{clean_name}_edited.jpg')