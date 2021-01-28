from statistics import mean

from utils import calc_pixel_brightness

from collections import namedtuple

Pixel = namedtuple("Pixel","red,green,blue")

pixel = Pixel(100, 0, 0)
pixel2 = Pixel(blue=0, red=50, green=100)
print(pixel)
print(pixel2)

pixel_brightness = calc_pixel_brightness(pixel.red, pixel.green, pixel.blue)
pixel_brightness2 = calc_pixel_brightness(pixel2[0], pixel2[1], pixel2[2])


mean_brightness = mean([pixel_brightness, pixel_brightness2])
print(mean_brightness)


