import numpy
from statistics import mean

from models import Pixel

pixel = Pixel(100, 0, -10)
pixel2 = Pixel(red=50, green=100, blue=0)

mean_brightness = mean([pixel.brightness, pixel2.brightness])
print(mean_brightness)
print("Done!")
print("Step1")
print("Step2")
