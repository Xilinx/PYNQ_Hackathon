from pynq.overlays.base import BaseOverlay
import numpy as np
import matplotlib.pyplot as plt
import wave



"""
Create sin waves in the .pdm format for use by the demo.
Apparently the Pynq can only read from files such as these .pdms,
so we create very short clips 
"""

print("Init overlay")
base = BaseOverlay("base.bit")
pAudio = base.audio
print("Init audio")


fs           = 44100   # sampling rate, Hz, must be integer
duration     = 1.0/5.0 # in seconds, may be float
f            = 440.0   # sine frequency, Hz, may be float
scale_factor = 32270   # set a scale factor to vaguely 1/2 of maxint

# pentatonic keys and respective output filenames
keys = [184.997, 207.652, 233.082, 277.183, 311.127, 369.994, 830.609, 932.328 ]
filenames = ["Gb3.pdm", "Ab4.pdm", "Bb4.pdm", "Db4.pdm", "Eb4.pdm", "Gb4.pdm", "Ab5.pdm", "Bb5.pdm" ]

print("initialize buffer")
num_samples = int(duration*fs)
mybuffer = np.zeros(num_samples, dtype=np.int16)

for idx in range(len(keys)):

	print("Creating Key %s" %(filenames[idx]))
	for j in range(num_samples):
		mybuffer[j] = scale_factor* np.sin(2*np.pi*keys[idx]*j/fs)

	for k in range(1, num_samples-1):
		print(mybuffer[k])
		if mybuffer[k] > 0 and mybuffer[k-1] < 0:
			startidx = k
			print("found start index")
			print(startidx)
			break	

	for l in range(num_samples-1, 1, -1):
		print(mybuffer[l])
		if mybuffer[l] > 0 and mybuffer[l-1] < 0:
			endidx = l
			print("found end index")
			print(endidx)
			break

	mybuffer = mybuffer[startidx:endidx]
	mybuffer[-1] = mybuffer[0]
	num_samples = len(mybuffer)

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

# not sure if this is useful
pAudio.close()

