import waveFunctions as b
import spidev
import time
import RPi.GPIO as GPIO
import numpy as np
import time

spi = spidev.SpiDev()

b.initSpiAdc()
measure_x = []
t0 = time.time()
t = t0
while t - t0 < 10:
    t = time.time()
    measure_x.append(b.getAdc())

b.deinitSpiAdc()

b.save(measure_x, t0, t)
