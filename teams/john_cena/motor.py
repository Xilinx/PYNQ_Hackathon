from pynq.overlays.base import BaseOverlay
from time import sleep
from pynq.lib.arduino.arduino_ardumoto import Arduino_Ardumoto
    
class motor:


    def __init__(self):
        # Motor stuff
        self.base = BaseOverlay("base.bit")
        self.ardu = Arduino_Ardumoto(self.base.ARDUINO)
        self.ardu.configure_pins(self.ardu.defaultpins)
        self.ardu.configure_polarity(self.ardu.motorB, self.ardu.pol_reverse)
        self.ardu.configure_polarity(self.ardu.motorA, self.ardu.pol_reverse)
        # Range finder stuff


    def turn_left (self,degree):
            self.ardu.set_speed(self.ardu.motorA,70)
            self.ardu.set_speed(self.ardu.motorB,70)
            self.ardu.set_dir(self.ardu.motorA, self.ardu.forward)
            self.ardu.set_dir(self.ardu.motorB, self.ardu.backward)
            self.ardu.run(self.ardu.motorA)
            self.ardu.run(self.ardu.motorB)
            for time in range (0, degree):
                    sleep (0.5)
            #self.ardu.stop(self.ardu.motorA)
            #self.ardu.stop(self.ardu.motorB)

    def turn_right (self,degree):
            self.ardu.set_speed(self.ardu.motorA,70)
            self.ardu.set_speed(self.ardu.motorB,70)
            self.ardu.set_dir(self.ardu.motorA, self.ardu.backward)
            self.ardu.set_dir(self.ardu.motorB, self.ardu.forward)
            self.ardu.run(self.ardu.motorA)
            self.ardu.run(self.ardu.motorB)
            for time in range (0, degree):
                    sleep (0.5)
            #self.ardu.stop(self.ardu.motorA)
            #self.ardu.stop(self.ardu.motorB)

    def forward (self,duration):
            self.ardu.set_speed(self.ardu.motorA,70)
            self.ardu.set_speed(self.ardu.motorB,70)
            self.ardu.set_dir(self.ardu.motorA, self.ardu.forward)
            self.ardu.set_dir(self.ardu.motorB, self.ardu.forward)
            self.ardu.run(self.ardu.motorA)
            self.ardu.run(self.ardu.motorB)
            for time in range (0, duration):
                    sleep (0.5)
            #self.ardu.stop(self.ardu.motorA)
            #self.ardu.stop(self.ardu.motorB)

    def backward (self,duration):
            self.ardu.set_speed(self.ardu.motorA,70)
            self.ardu.set_speed(self.ardu.motorB,70)
            self.ardu.set_dir(self.ardu.motorA, self.ardu.backward)
            self.ardu.set_dir(self.ardu.motorB, self.ardu.backward)
            self.ardu.run(self.ardu.motorA)
            self.ardu.run(self.ardu.motorB)
            for time in range (0, duration):
                    sleep (0.5)
            #self.ardu.stop(self.ardu.motorA)
            #self.ardu.stop(self.ardu.motorB)
            
    def stop (self):
            self.ardu.stop(self.ardu.motorA)
            self.ardu.stop(self.ardu.motorB)

