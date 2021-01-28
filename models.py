from dataclasses import dataclass

from utils import calc_pixel_brightness


class Pixel:

    def __init__(self, red: float, green: float, blue: float):
        self.red = red
        self.green = green
        self.blue = blue
        self.validate()

    def validate(self):
        if self.red < 0 or self.green < 0 or self.blue < 0:
            raise ValueError("Color channels cannot be negative!")

    @property
    def brightness(self):
        return calc_pixel_brightness(r=self.red, g=self.green, b=self.blue)