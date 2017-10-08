from pynq.overlays.base import BaseOverlay
from time import sleep
base = BaseOverlay("base.bit")
pAudio = base.audio

pAudio.load("notes/Gb3.pdm")
pAudio.play()

sleep(2)

pAudio.load("notes/Ab4.pdm")
pAudio.play()

sleep(2)

pAudio.load("notes/Bb4.pdm")
pAudio.play()

sleep(2)

pAudio.load("notes/Db4.pdm")
pAudio.play()

sleep(2)

pAudio.load("notes/Eb4.pdm")
pAudio.play()

sleep(2)

pAudio.load("notes/Gb4.pdm")
pAudio.play()

