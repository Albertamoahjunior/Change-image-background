import os
from PIL import Image, ImageDraw, ImageFilter
from rembg import remove


#folder to keep raw images
DIR_PATH_INPUT = r'C:\Users\ALBERT AMOAH JUNIOR\Desktop\hoodies\rawImages'

#directory to keep editted images
DIR_PATH_OUTPUT = r'C:\Users\ALBERT AMOAH JUNIOR\Desktop\hoodies\editedImages'


#Source for background images
background = Image.open(r"C:\Users\ALBERT AMOAH JUNIOR\Desktop\hoodies\back.jpg")
output_name = "\image"
output_path = DIR_PATH_OUTPUT + output_name
image_number = 0


raw_images = os.listdir(DIR_PATH_INPUT)

for image in raw_images:
    image_number += 1
    output_path += str(image_number)
    #make path for all the photos in input path
    image_path = os.path.join(DIR_PATH_INPUT, image)
    image_use = Image.open(image_path)
    #remove background for each photo
    no_background_image = remove(image_use, alpha_matting=True, alpha_matting_background_threshold=10, alpha_matting_erode_size=10, alpha_matting_foreground_threshold=240)

    #paste the image on the background
    background_copy = background.copy()
    background_copy.paste(no_background_image, (100, 50), no_background_image)
    foutput_path = output_path + ".jpg"
    background_copy.save(foutput_path)


