
from PIL import Image
import numpy as np
import cv2

	

def showsize ():
	im = Image.open('personal-03-crop.jpg')
	width, height = im.size
	print(width, height)

def resize():
	img = Image.open("personal-03.jpg")
	width, height = img.size
	new_width  = 563
	new_height = 690
	new_width  = new_height * width / height
	new_height = new_width * height / width 
	img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
	img.save("personal-03-resize.jpg")
	
def crop_image(input_image, output_image, start_x, start_y, width, height):
    input_img = Image.open(input_image)
    box = (start_x, start_y, start_x + width, start_y + height)
    output_img = input_img.crop(box)
    output_img.save(output_image + ".jpg")

def crop():
	image  = Image.open('personal-05.jpg')
	width  = image.size[0]
	height = image.size[1]

	aspect = width / float(height)

	ideal_width = 563
	ideal_height = 690

	ideal_aspect = ideal_width / float(ideal_height)

	if aspect > ideal_aspect:
		# Then crop the left and right edges:
		new_width = int(ideal_aspect * height)
		offset = (width - new_width) / 2
		resize = (offset, 0, width - offset, height)
	else:
		# ... crop the top and bottom:
		new_height = int(width / ideal_aspect)
		offset = (height - new_height) / 2
		resize = (0, offset, width, height - offset)

	thumb = image.crop(resize).resize((ideal_width, ideal_height), Image.ANTIALIAS)
	thumb.save('personal-05.jpg')


#showsize()
crop()
#crop_image("personal-03.jpg","personal-03-crop_image.jpg", 0, 0, 563, 690)
#resize()


