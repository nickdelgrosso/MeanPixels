from copy import copy
from statistics import mean
from typing import List, NamedTuple

from utils import calc_pixel_brightness

from dataclasses import dataclass, field

@dataclass(frozen=False)
class Pixel:
    red: List = field(repr=False, default_factory=list)
    green: List = field(default_factory=list)
    blue: List = field(default_factory=list)

pixel = Pixel()
pixel.red = [2, 3, 4]


pixel2 = Pixel()
print(pixel)
print(pixel2)
# print(pixel, pixel2)


#
# pixel = Pixel(100, 0, 0)
# pixel2 = Pixel(red=50, green=100)
# print(pixel)
# print(pixel2)
#
# pixel_brightness = calc_pixel_brightness(pixel.red, pixel.green, pixel.blue)
# pixel_brightness2 = calc_pixel_brightness(pixel2.red, pixel2.green, pixel2.blue)
#
# mean_brightness = mean([pixel_brightness, pixel_brightness2])
# print(mean_brightness)
