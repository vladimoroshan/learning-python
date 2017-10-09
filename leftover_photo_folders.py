#! python3
""" Find a leftover photo folders.
    Program that goes through every folder on your hard drive and finds potential photo folders 
    File must have the file extension .png or .jpg. 
    Photos a large images, so width and height must be larger than 500 pixels. 
    This is a safe bet, since most digital camera photos are several thousand pixels 
    in width and height. And at least 10 photos should be in a folder to show up in result 
"""

import os
from PIL import Image

root = os.environ["HOME"] # for Windows use 'C:\\'
minNumberOfPhotos = 10 

for foldername, subfolders, filenames in os.walk(root): 
    numPhotoFiles = 0
    numNonPhotoFiles = 0    
    for filename in filenames:    	
    	print('Processing...')
        # Check if file extension isn't .png or .jpg.
        if not (filename.endswith('.png') or filename.endswith('.jpg')):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        img = Image.open(foldername + '/' + filename)
        img_width, img_height = img.size

        if img_width > 500 and img_height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos
    if numPhotoFiles > numNonPhotoFiles and numPhotoFiles > minNumberOfPhotos:
        print('Check out folder with images in: ' + foldername + '/' + filename + '\n')

   


