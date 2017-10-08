## Sonic LIGO
A sound localizer inspired by the LIGO gravitational wave detector.  
By setting up sound sensors in an "L" shape, the system localizes sound origin by quadrant.

### Members
Team Daedalus are:

* Carl Bruce
* Dixon Dick
* Jordan Dick

### PYNQ Board Requirement
PYNQ sensors present a unique opportunity to run a standard ARM core with Ubuntu Linux  
as well as advanced audio processing using FPGA native functionality for speed at low power.  

The scipy library is used for convolutions used to detect sharp sounds, as well as determine  
peak timing, in order to determine distance. So time and frequency domain are both in play.

### Files
daedalus_clap_detector.ipynb - Main Python Notebook  

### Photos
* PYNQ Block Design.png
* Team Table.png
* Battery Power.png

### Screenshots
The input to the detector is shown as well as the convolutional result.  

* detector_input.png
* detector_output.png
