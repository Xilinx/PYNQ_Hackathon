# **OpenCV Air Keyboard**

## Welcome to our Xilinx hackathon 2017 repository!

### Team Members
```
Chase Stewart
Snehal Sanghvi
Spencer Arrasmith
Akshit Shah
```

### Description
```
Our team had collaborated together for this 30-hour hackathon to come up with something that was exciting and gave us an opportunity to hack our way through a Xilinx Pynq development FPGA kit to develop a cool and functional project.

Our application is an air piano / virtual piano that allows the user to just press some virtual key which will be picked up by our image processing program and will output a unique musical note. As mentioned above, we used the Pynq development board from Xilinx which allowed us to program our FPGA at a higher level of abstraction using the Python API. 

In terms of external peripherals used, we made use of a HDMI out cable to send the image frame to be displayed on a monitor and a camera module to give us a continous stream of image frames. Since our project broadly delved into the two domains of video and audio, sending and receiving data to and from the HDMI, we decided to make use of 2 threads to allow for concurrent execution of our model. A single line of flow would have meant increased latencies and a reduced effective frame rate (in effect taking out the 'fun' from actually dealing with something as fun).

For purpose of demonstration for the hackathon, we designed 8 discrete keys that could be 'pressed' (its all virtual!) that would produce distinct musical notes for the user, akin to playing a piano. In order to go about the process, we first divided our screen into 8 distinct spaces corresponding to the keys and performed several image processing manourevres on the image frames to detect human hand motion in the space. Some of the processing we did was to perform a RGB to GRAY conversion, resizing the image and calculating the differences of the current frame from the first obtained frame. This difference encodes the change that has happened since and it corresponds to the human hand pressing a particular key. This allows us to identify the key intended to be presseD and is used by our audio generating program (essentially a separate thread) to play the corresponding note. There is some dilation performed on the image to plug the gaps and after identifying the biggest contour, we design a bounding box around it to indicate the human hand. We calculate the centroid of the detected contour to decide which region it falls in.  

At the lower (yet abstracted level), we make use of overlays or bitstreams, which are essentially equivalent to IP cores in the more traditional sense of FPGAs. Using the Base overlay of the Pynq board, a lot of the lower level headaches of FPGAs has been removed. The audio files essentially have musical notes of pre-defined frequencies that make use of the Audio module. Getting the audio and video modules to work concurrently was a challenge and the use of threads made this application smooth, functional and more modular in general.
```

### Citation
```
It relies heavily on the work of Adrian Rosebrock to do motion detection from video.
(https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/)
```

### Licencing
```
This code is Open-Sourced and is compatible with the Jupyter notebook project. 
We have made an effort to develop this project to be as modular as well and 
we hope other developers will build of of this code and suggest us on how to improve upon the application. 
```

### RunMe:
```
$ sudo python3.6 gen_samples.py
$ sudo python3.6 webcam.py
```
