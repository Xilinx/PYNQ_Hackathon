# Xilinx_Hackathon
Joy of Pynq 

#Purpose 
Contribution towards the new Xilinx's PYNQ open source paltform in the 2017 Xilinx "Professional, Invite only Hackathon" 

#Brief
We are CU boulder student we believe that expression emption through animojis is the way to go.
The members of the team are Bhallaji Venkatesan, Mounika edula Redddy, Sahana Sadagopan , Divya Kumar Sampath.

#Project 
We have developed a fullstack project that leverages the programmable capabilities of the new open-source Xilinx PYNQ Project to implement a similar concept to APPLE INC's Animojis, that captures video through the usb camera and processes the data which is streamed out
through the HDMI out port. The data captured from the usb Camera is being sent to the Azuze Emotion API (https://docs.microsoft.com/en-us/azure/)
which runs at high performance 
output. 
We have developed a project to classify 7 major emotion classifications in humans namely
ANGER
Happiness 
Sadness
Surprise
contempt
disgust
fear

#Usage 
Login to the Junyper Notebook in the following location and execute according your custom will.

The source code is stored in ~/jupyternotebook/base/opencv/PYNQ_Animoji.py

The following packages are to be installed to run the caffes network

Please follow the following Github Link : https://github.com/awai54st/PYNQ-Classification

#PYNQ USAGE 
1. Interface the pynq board via, the serial USB, Ethernet (with static IP : 192.168.2.99) and USB Wi-Fi dongle (if necessary)
2. Login to the Jupyter Notebook from the static IP, by configuring your network adapter setting to the same subnet as the static IP of the PYNQ board.
3. Login to the Jupter Notebook with the following credentials : 
Password : xilinx
4. Open the Jupyter Notebook Terminal and configure your USB Wi-Fi dongle (if used) in /common/usb-wifi.ipynb to setup WLAN on the board.
5. Open Jupyter Notebooks through your newly configured WLAN / leverage the use of SSH into the Jupter Notebook.


#Requiremnts 
Please run all the file and install all the modules on Python 3.6 and pip3.6 exclusively.


Check the JOY FOR PYNQ  notebook .
Basic setup:
connect the USB camera to the usb Port of the HDMI cable 
connect the HDMI ouput to a monitor/PC.
Download the above mentioned notebook

