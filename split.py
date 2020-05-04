import cv2
import os
import shutil

from pathlib import Path
import shutil


def splitIntoFrames(fileName):
	dirpath = Path(os.getcwd(), 'frames')
	if dirpath.exists() and dirpath.is_dir():
	    shutil.rmtree(dirpath)

	os.mkdir('frames')

	print('CV2 Version: ', cv2.__version__)
	vidcap = cv2.VideoCapture(fileName)
	success,image = vidcap.read()
	count = 0
	while success:
	  cv2.imwrite(os.path.join(os.getcwd(), "frames/frame%d.jpg" % count), image) 
	  success,image = vidcap.read()
	  print ('Writing a new frame: %d' % count, success)
	  count += 1
