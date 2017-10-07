from pynq.overlays.base import BaseOverlay
import numpy as np
import matplotlib.pyplot as plt
import wave

#print("Init overlay")
base = BaseOverlay("base.bit")
pAudio = base.audio
#print("Init audio")

fs = 44100          # sampling rate, Hz, must be integer
duration =1.0/5.0   # in seconds, may be float
f = 440.0           # sine frequency, Hz, may be float

keys = [184.997, 207.652, 233.082, 277.183, 311.127, 369.994 ]
filenames = ["Gb3.pdm", "Ab4.pdm", "Bb4.pdm", "Db4.pdm", "Eb4.pdm", "Gb4.pdm" ]

num_samples = int(duration*fs)

#print("init buffer")
mybuffer = np.zeros(num_samples, dtype=np.int16)

for idx in range(len(keys)):
	#print("Creating Key %s" %(keys[idx]))
	for j in range(num_samples):
		mybuffer[j] = 32270* np.sin(2*np.pi*keys[idx]*j/fs)

	with wave.open("notes/"+filenames[idx], 'wb') as pdm_file:
	    # Set the number of channels
	    pdm_file.setnchannels(1)
	    # Set the sample width to 2 bytes (16 bit)
	    pdm_file.setsampwidth(2)
	    # Set the frame rate to sample_rate
	    pdm_file.setframerate(fs)
	    # Set the number of frames to sample_len
	    pdm_file.setnframes(num_samples)
	    # Set the compression type and description
	    pdm_file.setcomptype('NONE', "not compressed")
	    # Write data
	    pdm_file.writeframes(mybuffer.astype(np.int16))

pAudio.close()



