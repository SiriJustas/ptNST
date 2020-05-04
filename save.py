import cv2
import glob
import os

from pathlib import Path
import shutil

from os import walk

def  saveVideo(frameR):
	dirpath = Path(os.getcwd(), 'output')
	if dirpath.exists() and dirpath.is_dir():
	    shutil.rmtree(dirpath)

	os.mkdir('output')

	print('Starting to merge frames')
	img_array = []
	for filename in sorted(glob.glob('frames/*.jpg'), key=os.path.getmtime):
	    img = cv2.imread(filename)
	    print(filename)
	    height, width, layers = img.shape
	    size = (width,height)
	    img_array.append(img)
	 
	out = cv2.VideoWriter("output/outputvideo.avi",cv2.VideoWriter_fourcc(*'XVID'), frameR, size)
	 
	for i in range(len(img_array)):
	    out.write(img_array[i])
	out.release()

