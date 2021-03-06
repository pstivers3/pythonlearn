# Use Python Image Library (PIL) to crop and annotate an image.

import Image, ImageDraw, ImageFont
import os, sys


img_file = 'sim3109.png'

# Identify regions of interest
crop_pos = (764, 326)       #(x, y) of upper right corner
crop_size = (501, 433)      #(length, width)
crop_box = (crop_pos[0], crop_pos[1], crop_pos[0] + crop_size[0],
            crop_pos[1] + crop_size[1])

print 'crop_box = %s' % str(crop_box)

# Get image, crop it
im = Image.open(img_file)
cropped_im = im.crop(crop_box)

cropped_im.save('sim3109_crop.png')
print 'sim3109_crop.png saved!'

# TODO
#   - Use Image.copy() to get a copy of original image.
#     and crop it to the title area (says 'A3300 die3 ...')
#     and Image.paste() it to cropped_im and save.
#       * title_pos = (25, 274)
#       * title_size = (400, 47)

# Bonus
#   - Use Image.size() property to center the pasted image.


# Identify regions of interest
crop_pos = (25, 274)       #(x, y) of upper right corner
crop_size = (400, 47)      #(length, width)
crop_box = (crop_pos[0], crop_pos[1], crop_pos[0] + crop_size[0],
            crop_pos[1] + crop_size[1])

title_im = im.copy()
title_im = title_im.crop(crop_box)

x_pos = 10
# Bonus:
# x_pos = int(cropped_im.size[0] / 2 - title_im.size[0] / 2)
y_pos = 10
cropped_im.paste(title_im, (x_pos, y_pos))

cropped_im.save('sim3109_paste.png')
print 'sim3109_paste.png saved!'                 
