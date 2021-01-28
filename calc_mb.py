red = 100  # Red value
red2 = 50

green = 0  # Green value
green2 = 100

blue = 0  # Blue value
blue2 = 0

readiness = 0  # Readiness value
readiness2 = 200

def get_pixel_brightness(r, g, b):
    return (r + g + b) / 3

# Get pixel brightnesses
pixel_brightness = get_pixel_brightness(red, green, blue)
pixel_brightness2 = get_pixel_brightness(red2, green2, blue2)


# Get mean brightness
mean_brightness = (pixel_brightness + pixel_brightness2) / 2
print(mean_brightness)


