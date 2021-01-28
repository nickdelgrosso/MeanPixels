from statistics import mean

from models import Pixel


pixel = Pixel(100, 0, 0)
pixel2 = Pixel(red=50, green=100, blue=0)

mean_brightness = mean([pixel.brightness, pixel2.brightness])
print(mean_brightness)
