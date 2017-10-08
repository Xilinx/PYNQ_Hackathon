#!/usr/bin/python3.6

from pynq.overlays.base import BaseOverlay
from pynq.lib.video import *
import numpy as np
from pynq import Xlnk
import time
import cv2

xlnk = Xlnk()
xlnk.xlnk_reset()

base = BaseOverlay("base.bit")

face_cascade = cv2.CascadeClassifier(
    '/home/xilinx/jupyter_notebooks/base/video/data/'
    'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(
    '/home/xilinx/jupyter_notebooks/base/video/data/'
    'haarcascade_smile.xml')

frame_w = 640 
frame_h = 480

Mode = VideoMode(frame_w, frame_h, 24) 
hdmi_out = base.video.hdmi_out
hdmi_out.configure(Mode, PIXEL_BGR)
hdmi_out.start()

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Capture device is open? " + str(cap.isOpened()))

#Global Vars
start_recording = False
trigger_time = 0 #Hold timestamp of the last detection

num_smiles = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')  
writer = None
# Facial and Smile recognition:


try:
    started = time.time()
    while base.buttons[1].read()==0:
            ret, frame_vga = cap.read()
            if (ret):
                """
                outframe = hdmi_out.newframe()
                outframe[:] = frame_vga
                hdmi_out.writeframe(outframe)
                """
                
                np_frame = frame_vga
                
                instant = time.time() # get timestamp of the frame

                      
                gray = cv2.cvtColor(np_frame, cv2.COLOR_BGR2GRAY)
                

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x,y,w,h) in faces:
                    cv2.rectangle(np_frame,(x,y),(x+w,y+h),(255,0,0),2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = np_frame[y:y+h, x:x+w]
                    """
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex,ey,ew,eh) in eyes:
                        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    """
                    smiles = smile_cascade.detectMultiScale(
                        roi_gray,
                        scaleFactor= 1.7,
                        minNeighbors=22,
                        minSize=(25, 25),
                        flags=cv2.CASCADE_SCALE_IMAGE
                    )
                    for (sx,sy,sw,sh) in smiles:
                        print("Found", len(smiles), "smile(s).")
                        cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (255, 0,0), 1)
                        #display number of smile on frame:
                        text_font = cv2.FONT_HERSHEY_SIMPLEX
                        bottomLeftCornerOfText = (0,300)
                        fontScale = 1
                        fontColor = (255,255,255)
                        lineType = 2        
                        cv2.putText(np_frame,"Found {} smile(s)!".format(len(smiles)), 
                            bottomLeftCornerOfText, 
                            text_font, 
                            fontScale,
                            fontColor,
                            lineType)
                    if len(smiles) > 0:
                        if writer is None:
                            writer =cv2.VideoWriter('capture_moments/'+time.strftime("%Y%m%d-%H%M%S") + '.avi',fourcc, 2.5, (frame_w,frame_h))

                        num_smiles = len(smiles)
                        trigger_time = instant
                        start_recording = True
                    if start_recording and instant <= trigger_time + 30:
                        writer.write(frame_vga)
                        print("writing because ", instant, trigger_time + 10)
                    else:
                        print("STOP RECORDING")
                        start_recording = False
                        if writer is not None:
                            writer.release()
                            writer = None
                        
                        #capture_video('captured_moments', 5)
                        
                        # capture smiling images
                        #cv2.imwrite('capture_moments/' + time.strftime("%Y%m%d-%H%M%S") + '.jpg', frame_vga)
                        

                # Output OpenCV results via HDMI
                outframe = hdmi_out.newframe()
                outframe[0:480,0:640,:] = frame_vga[0:480,0:640,:]

                #outframe = hdmi_out.newframe()
                #outframe[:] = frame
                
                hdmi_out.writeframe(outframe)
                
            else:
                raise RuntimeError("Error while reading from camera")
finally:
    print("Cancel")
    hdmi_out.stop()
    cap.release()
    if writer is not None:
        writer.release()
    cv2.destroyAllWindows()