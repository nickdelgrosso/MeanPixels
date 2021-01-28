from dataclasses import dataclass

from utils import calc_pixel_brightness


@dataclass(frozen=True)
class Pixel:
    red: float
    green: float
    blue: float

    @property
    def brightness(self):
        return calc_pixel_brightness(r=self.red, g=self.green, b=self.blue)