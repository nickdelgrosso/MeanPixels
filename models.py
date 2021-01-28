from dataclasses import dataclass

from utils import calc_pixel_brightness


@dataclass(frozen=True)
class Pixel:
    red: float
    green: float
    blue: float

    def __post_init__(self):
        self.validate()

    def validate(self):
        if self.red < 0 or self.green < 0 or self.blue < 0:
            raise ValueError("Color channels cannot be negative!")

    @property
    def brightness(self):
        return calc_pixel_brightness(r=self.red, g=self.green, b=self.blue)