from pynq.overlays.base import BaseOverlay
from pynq.lib.video import *
from matplotlib import pyplot as plt
import numpy as np

import cv2

base = BaseOverlay("base.bit")
# monitor configuration: 640*480 @ 60Hz
Mode = VideoMode(640,480,24)
hdmi_out = base.video.hdmi_out

hdmi_out.configure(Mode,PIXEL_BGR)
hdmi_out.start()
# monitor (output) frame buffer size
frame_out_w = 1920
frame_out_h = 1080
# camera (input) configuration
frame_in_w = 640
frame_in_h = 480


videoIn = cv2.VideoCapture(0)
videoIn.set(cv2.CAP_PROP_FRAME_WIDTH, frame_in_w);
videoIn.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_in_h);

print("Capture device is open: " + str(videoIn.isOpened()))

import numpy as np
import PIL
import pyscreenshot as ImageGrab
from pynq.lib.arduino import Grove_Buzzer
from pynq.lib.arduino import ARDUINO_GROVE_G1

# Display webcam image via HDMI Out
#imgemoji = cv2.imread('mj1.jpg',-1)
#orig_mask = imgemoji[:,:,2]
# Create the inverted mask for the mustache
#orig_mask_inv = cv2.bitwise_not(orig_mask)
#imgmj = imgemoji[:,:,0:2]
#origemojiHeight, origemojiWidth = imgmj.shape[:2]

while(True):
    ret, frame_vga = videoIn.read()
    if (ret):      
        np_frame = frame_vga
        face_cascade = cv2.CascadeClassifier(
            '/home/xilinx/jupyter_notebooks/base/video/data/'
            'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(np_frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(np_frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = np_frame[y:y+h, x:x+w]

        outframe = hdmi_out.newframe()
        outframe[0:480,0:640,:] = frame_vga[0:480,0:640,:]
        hdmi_out.writeframe(outframe)
        cv2.imwrite("frame.jpg",frame_vga)
        cv2.waitKey(50)
        
    else:
        raise RuntimeError("Failed to read from camera.")
        
#grove_buzzer = Grove_Buzzer(base.ARDUINO,ARDUINO_GROVE_G1)
#grove_buzzer.play_melody()        
