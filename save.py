import cv2
import glob
import os

from pathlib import Path
import shutil

from os import walk

def  saveVideo(frameR):
	print('Starting to merge frames into video \n')
	img_array = []
	for filename in sorted(glob.glob('output/*.png'), key=os.path.getmtime):
	    img = cv2.imread(filename)
	    print(filename)
	    height, width, layers = img.shape
	    size = (width,height)
	    img_array.append(img)
	 
	out = cv2.VideoWriter("output/outputvideo.avi",cv2.VideoWriter_fourcc(*'XVID'), frameR, size)
	 
	for i in range(len(img_array)):
	    out.write(img_array[i])
	out.release()

