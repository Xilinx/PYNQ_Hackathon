# Voice Controlled Mobile Robot
Team John Cena

## Objective
Our team's goal was to develop a mobile robot controlled completely by voice commands. 

## Utilized modules and resources
Three principal elements were involved in the project. These were developed in parallel, independently, in anticipation of being integrated into a wholistic control system at a later point in time. The resources and standalone modules that were combined in our final project were:

#### Command Source
* An operator issues commands from a location remote to the robot itself
* A headset was used to capture verbal commands issued by the operator
* WAV file creation was used to store the captured verbal commands to forward to the robot
* Command transmission was facilitated across the wireless network connection

#### ArduMoto Shield
* PWM to control two independently actuated wheels
* Full H-Bridge to drive the motors
* MicroBlaze Soft Processor control

#### Python Verbalizer and Speech Processor
* Python SpeechRecognition library parses and interprets contents of WAV file received from Command Source
* Output text is compared against an array of supported commands
* Appropriate signal is sent to robotic motion controller

## Implementation
We developed a robot on two wheels that is remotely connected to a command source. This robot can follow a course of motion delineated by a human operator at that command source, using only verbal commands to communicate. The available motion commands include Forward, Backward, Left, Right.

## Results
Despite our lack of Python knowledge, we were able to overcome this and create a functioning design leveraging both the processing power and capabiliy of the Zynq 7020.

## How to Reproduce
Our project can be rebuilt using the pip utility and Jupyter. After connecting to the Pynq board and loading this repository, the project may be run by following these steps:
1) Setup a command controller with a microphone input to capture vocal commands. These audio files may be captured and stored to an audio (WAV) file using the ALSA arecord utility.
2) The command controller must have a mechanism to interact with the robot such that it may periodically submit audio files as commands. We used a wireless network to facilitate this interaction.
3) A robot must be available with two wheels, a basic platform, and a housing (with mobile power supply) for the Pynq board to be attached to the robot. The Pynq board will receive verbal command files, translate them to motor actuation using the SpeechRecognition Python Library, and pause motion while anticipating the next incoming command.
4) Capture a command at the command controller.
5) Execute the robot control software by running Remote Voice-Controlled Robot.ipynb to master the onboard Arduino and to control the speech translation.
6) Continue issuing commands as long as desired.

7) Please review our code for further implementation questions.

# Thanks!
