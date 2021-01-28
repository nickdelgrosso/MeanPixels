from copy import copy
from statistics import mean
from typing import List, NamedTuple

from utils import calc_pixel_brightness

from dataclasses import dataclass


class Pixel:

    def __init__(self, red = None, green = None, blue = None):
        self.red = red if red is not None else []
        self.green = green if green is not None else []
        self.blue = blue if blue is not None else []

    def __add__(self, other):  # dunder methods
        return self.red + other.red

    def __str__(self):
        return f"Pixel(red={self.red}, green={self.blue}, blue={self.green})"

pixel = Pixel()
pixel.red.append(1)
pixel.red.append(2)


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
