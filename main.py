from statistics import mean

from models import Pixel
from dataclasses import asdict, astuple

pixel = Pixel(100, 0, 0)
print(pixel)

pd = asdict(pixel)
print(pd)

pt = astuple(pixel)
print(pt)

pixel2 = Pixel(red=50, green=100, blue=0)

mean_brightness = mean([pixel.brightness, pixel2.brightness])
print(mean_brightness)
