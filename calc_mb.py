from utils import calc_pixel_brightness

red = 100
red2 = 50

green = 0
green2 = 100

blue = 0
blue2 = 0

readiness = 0
readiness2 = 200

pixel_brightness = calc_pixel_brightness(red, green, blue)
pixel_brightness2 = calc_pixel_brightness(red2, green2, blue2)


mean_brightness = (pixel_brightness + pixel_brightness2) / 2
print(mean_brightness)


