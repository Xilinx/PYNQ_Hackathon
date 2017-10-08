from pynq.overlays.base import BaseOverlay
from pynq.lib.video import *
from pynq import PL
from PIL import Image as PIL_Image
import sys, cv2, math, copy
from time import time, sleep
import numpy as np
import datetime
import imutils
import threading 

# audio states
PLAY_NOTHING = 0
PLAY_KEY_1   = 1
PLAY_KEY_2   = 2
PLAY_KEY_3   = 3 
PLAY_KEY_4   = 4
PLAY_KEY_5   = 5
PLAY_KEY_6   = 6
PLAY_KEY_7   = 7
PLAY_KEY_8   = 8

# program states 
IS_RUNNING = 0
IS_STOPPED = 1

# program state variables
audio_life_state   = IS_RUNNING
program_is_running = IS_RUNNING
audio_out_state    = PLAY_NOTHING

DEBUG = False
KEYS = False


class NullDevice():
	"""
	dummy to eat up stdout, thanks to coreygoldberg.blogspot.com!
	http://coreygoldberg.blogspot.com/2009/05/python-redirect-or-turn-off-stdout-and.html
	"""
	def write(self,s):
		pass



def start_audio():
	"""
	Simple threaded program to play out the currently selected note
	(or no note at all) based on the currently detected key
	"""
	while audio_life_state == IS_RUNNING:
		if   audio_out_state == PLAY_KEY_1:
			audioout.load("notes/Gb3.pdm")
			audioout.play()

		elif audio_out_state == PLAY_KEY_2:
		       audioout.load("notes/Ab4.pdm")
		       audioout.play()

		elif audio_out_state == PLAY_KEY_3:
		       audioout.load("notes/Bb4.pdm")
		       audioout.play()

		elif audio_out_state == PLAY_KEY_4:
		       audioout.load("notes/Db4.pdm")
		       audioout.play()

		elif audio_out_state == PLAY_KEY_5:
		       audioout.load("notes/Eb4.pdm")
		       audioout.play()

		elif audio_out_state == PLAY_KEY_6:
		       audioout.load("notes/Gb4.pdm")
		       audioout.play()

		elif audio_out_state == PLAY_KEY_7:
		       audioout.load("notes/Ab5.pdm")
		       audioout.play()

		elif audio_out_state == PLAY_KEY_8:
		       audioout.load("notes/Bb5.pdm")
		       audioout.play()
		
		elif audio_out_state == PLAY_NOTHING:
			pass
		
		sleep(0.0000001)

	print("Program is over, killing thread")
	return



#initialize audio
base = BaseOverlay("base.bit")
audioout = base.audio

# initialize output HDMI stream
my_mode = VideoMode(640, 480, 24)
hdmi_out = base.video.hdmi_out
hdmi_out.configure(my_mode, None ) 
hdmi_out.start()
print("Initialize output_HDMI")

# initialize input USB video capture
video_in = cv2.VideoCapture(0)
video_in.set(cv2.CAP_PROP_FRAME_WIDTH,  640 )
video_in.set(cv2.CAP_PROP_FRAME_HEIGHT, 480 )
print("Initialize video")

# set video vars 
cap_region_x_begin=0.5  # start point/total width
cap_region_y_end=0.8    # start point/total width
threshold = 120         #  BINARY threshold
blurValue = 100         # GaussianBlur parameter
bgSubThreshold = 350

starttime = time()

# variables
isBgCaptured = 0       # bool, whether the background captured
triggerSwitch = False  # if true, keyborad simulator works

# initialize the first frame in the video stream
firstFrame = None

# load keyboard images
img_unpressed = cv2.imread("pics/unpressed.png",-1)
img_unpressed = cv2.resize(img_unpressed,(79,240),interpolation = cv2.INTER_AREA)
unpressed_height,unpressed_width = img_unpressed.shape[:2]
img_un_alpha = img_unpressed[:,:,3]/255.0

img_pressed = cv2.imread("pics/pressed.png",-1)
pressed_height,pressed_width = img_pressed.shape[:2]
print("Initialize video stream!")

original_stdout = sys.stdout
sys.stdout = NullDevice()

original_stderr = sys.stderr
sys.stderr = NullDevice()

try:
	""" 
	main loop- grab a frame from webcam, process it, push to HDMI
	"""

	# start the audio thread
	t = threading.Thread(target=start_audio)
	t.start()

	while program_is_running == IS_RUNNING:
		start = time()
		retcode, frame_vga = video_in.read()

		# if the first frame is None, initialize it
		if firstFrame is None: 
			# first frame is used for comparison 
			outframe = hdmi_out.newframe()
			outframe[0:480, 0:640,:] = frame_vga[0:480,0:640,:]
			outframe1 = cv2.cvtColor(outframe, cv2.COLOR_RGB2GRAY)
			outframe1 = imutils.resize(outframe1,height=480,width=640)
			firstFrame = outframe
			continue
			
		elif retcode == True:
			outframe = hdmi_out.newframe()
		
			# create a copy-frame to manipulate 
			outframe[0:480, 0:640,:] = frame_vga[0:480,0:640,:]
			
			#outframe = imutils.resize(outframe, width=500)
			gray = cv2.cvtColor(outframe, cv2.COLOR_RGB2GRAY)
			gray = imutils.resize(gray,height=480,width=640)
			alpha_out = 1-img_un_alpha

			# draw 8 keys on the screen 
			if KEYS:
				for i in range(8):
					for c in range(3):
						outframe[120:120+unpressed_height,18+75*i:18+unpressed_width+75*i,c] = (img_un_alpha * img_unpressed[:,:,c]+alpha_out*outframe[120:120+unpressed_height,18+75*i:18+unpressed_width+75*i,c])
			
			# compute the absolute difference between the current frame and
			# first frame
			frameDelta = cv2.absdiff(outframe1, gray)
			thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
 
			# dilate the thresholded image to fill in holes, then find contours
			# on thresholded image
			thresh = cv2.dilate(thresh, None, iterations=2)
			(im2, contours, hierarchy) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			 
			# compute the bounding box for the contour, draw it on the frame,
			# and update the text
			for c in contours:
				# if the contour is too small, ignore it
				if cv2.contourArea(c) < 10000:
					continue
				x, y, w, h = cv2.boundingRect(c)
				if DEBUG:
					cv2.rectangle(outframe, (x, y), (x + w, y + h), (255, 0, 0), 2)
				M = cv2.moments(c)

				"""
				this is the key part of the algorithm
				compute the centroid of the motion object and
				determine whether it falls within a "key"
				"""				
				centroid_x = int(M['m10']/M['m00'])
				centroid_y = int(M['m01']/M['m00'])

				if DEBUG:
					print(centroid_x)
					print(centroid_y)
			

				# if the centroid is within a key, update audio state
				if(centroid_y > 180 and centroid_y < 420):
				# detect key 1 
					if(centroid_x > 20 and centroid_x < 95):
						audio_out_state = PLAY_KEY_1
						cv2.rectangle(outframe,(20,120),(95,360),(0,255,255),2)
					# detect key 2 
					elif(centroid_x < 170):
						audio_out_state = PLAY_KEY_2
						cv2.rectangle(outframe,(95,120),(170,360),(255,0,255),2)
					# detect key 3
					elif(centroid_x < 245):
						audio_out_state = PLAY_KEY_3
						cv2.rectangle(outframe,(170,120),(245,360),(255,255,0),2)
					# detect key 4
					elif(centroid_x < 320):
						audio_out_state = PLAY_KEY_4
						cv2.rectangle(outframe,(245,120),(320,360),(255,0,0),2)
					# detect key 5
					elif(centroid_x < 395):
						audio_out_state = PLAY_KEY_5
						cv2.rectangle(outframe,(320,120),(395,360),(0,255,0),2)
					# detect key 6
					elif(centroid_x < 470):
						audio_out_state = PLAY_KEY_6
						cv2.rectangle(outframe,(395,120),(470,360),(0,255,255),2)
					# detect key 7
					elif(centroid_x < 545):
						audio_out_state = PLAY_KEY_7
						cv2.rectangle(outframe,(470,120),(545,360),(255,0,255),2)
					# detect key 8
					elif(centroid_x < 620):
						audio_out_state = PLAY_KEY_8
						cv2.rectangle(outframe,(545,120),(620,360),(255,255,0),2)
				# else play nothing 
				else:
					audio_out_state = PLAY_NOTHING

			hdmi_out.writeframe(outframe)	

		# If capturing a frame fails. print a debug
		else:
			print("Failed!")
			#break
		
		# Run for 40s, then break
		if (time()-starttime > 600 ):
			sys.stdout = original_stdout
			sys.stderr = original_stderr
			print("Timeout- terminate program")
			program_is_running = IS_STOPPED
			audio_life_state = IS_STOPPED

	# after 30s, close the stream
	audio_life_state = IS_STOPPED
	t.join()
	print("Closing, goodbye!")
	video_in.release()
	hdmi_out.stop()
	del video_in
	del hdmi_out
	sys.exit()

# TODO we wish this would work but jupyter is handling SIGINT 
except KeyboardInterrupt:
	t.join()
	print("Goodbye:keyboard")
	video_in.release()
	hdmi_out.stop()
	del hdmi_out
	del video_in
	sys.exit()
	
# exit gracefully in case of a runtime error 
except RuntimeError as e:
	print("Goodbye:runtime")
	print(e)
	video_in.release()
	hdmi_out.stop()
	del hdmi_out
	del video_in
	t.join()
	#del audioout
	sys.exit()
