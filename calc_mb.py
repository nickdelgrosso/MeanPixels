from dataclasses import dataclass
from statistics import mean

from utils import calc_pixel_brightness


@dataclass(frozen=True)
class Pixel:
    red: float
    green: float
    blue: float

    @property
    def brightness(self):
        return calc_pixel_brightness(r=self.red, g=self.green, b=self.blue)



pixel = Pixel(100, 0, 0)
pixel2 = Pixel(red=50, green=100, blue=0)

mean_brightness = mean([pixel.brightness, pixel2.brightness])
print(mean_brightness)
