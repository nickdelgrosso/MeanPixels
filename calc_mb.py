from utils import calc_pixel_brightness


pixel = (100, 0, 0)
pixel2 = (50, 100, 0)

readiness = 0
readiness2 = 200

pixel_brightness = calc_pixel_brightness(pixel[0], pixel[1], pixel[2])
pixel_brightness2 = calc_pixel_brightness(pixel2[0], pixel2[1], pixel2[2])


mean_brightness = (pixel_brightness + pixel_brightness2) / 2
print(mean_brightness)


