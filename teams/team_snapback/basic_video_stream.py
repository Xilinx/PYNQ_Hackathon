#!/usr/bin/python3.6

from pynq.overlays.base import BaseOverlay
from pynq.lib.video import *
import numpy as np
import cv2

base = BaseOverlay("base.bit")

frame_w = 640 
frame_h = 480

Mode = VideoMode(frame_w, frame_h, 24) 
hdmi_out = base.video.hdmi_out
hdmi_out.configure(Mode, PIXEL_BGR)
hdmi_out.start()

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Capture device is open?: " + str(cap.isOpened()))


while True:
    ret, frame = cap.read()
    
    if ret:
        outframe = hdmi_out.newframe()
        outframe[:] = frame
        hdmi_out.writeframe(outframe)
    else:
        raise RuntimeError("Error while reading from camera")

cap.release()
cv2.destroyAllWindows()
