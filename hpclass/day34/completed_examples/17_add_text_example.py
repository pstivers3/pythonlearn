# Use Python Image Library (PIL) to add text to an image.

import Image, ImageDraw, ImageFont
import os, sys


img_file = 'sim3109.png'

# Identify regions of interest
crop_pos = (764, 326)       #(x, y) of upper right corner
crop_size = (501, 433)      #(length, width)
crop_box = (crop_pos[0], crop_pos[1], crop_pos[0] + crop_size[0],
            crop_pos[1] + crop_size[1])

# Get image, crop it
im = Image.open(img_file)
cropped_im = im.crop(crop_box)


# Add centered text title 
fontSize = 36
font = ImageFont.truetype('arial.ttf', fontSize)
draw = ImageDraw.Draw(cropped_im)
textSize = draw.textsize('Die 3', font=font)
x_pos = int(cropped_im.size[0] / 2 - textSize[0] / 2)
y_pos = 10
draw.text((x_pos, y_pos), 'Die 3', fill='black', font=font)


# TODO:
#   - Add file name to lower right corner.
#


# Add file name as watermark in lower right corner.
fontSize = 18
font = ImageFont.truetype('arial.ttf', fontSize)
draw = ImageDraw.Draw(cropped_im)
textSize = draw.textsize(img_file, font=font)
x_pos = cropped_im.size[0] - textSize[0] - 20
y_pos = cropped_im.size[1] - textSize[1] - 5
draw.text((x_pos, y_pos), img_file, fill='darkgrey', font=font)

cropped_im.save('sim3109_text.png')
print 'sim3109_text.png saved!'
