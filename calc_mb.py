from dataclasses import dataclass
from statistics import mean

from utils import calc_pixel_brightness


@dataclass(frozen=True)
class Pixel:
    red: float
    green: float
    blue: float

    def get_brightness(self):
        return calc_pixel_brightness(r=self.red, g=self.green, b=self.blue)



pixel = Pixel(100, 0, 0)
pixel2 = Pixel(red=50, green=100, blue=0)

pixel_brightness = pixel.get_brightness()
pixel_brightness2 = pixel2.get_brightness()

mean_brightness = mean([pixel_brightness, pixel_brightness2])
print(mean_brightness)
