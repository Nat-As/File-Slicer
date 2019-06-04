import sys
import argparse
import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
      success,image = vidcap.read()
      print ("Frame %d Created!" % count)
      cv2.imwrite( pathOut + "%d.jpg" % count, image)     # save frame as JPEG file
      count = count + 1
extractImages("Data/presenter.mp4", "img/presenter/Presenter")#presenter
#extractImages("Data/crowd.mp4", "img/crowd/Crowd")#crowd