red = 100  # Red value
red2 = 50

green = 0  # Green value
green2 = 100

blue = 0  # Blue value
blue2 = 0

readiness = 0  # Readiness value
readiness2 = 200

# Get pixel brightnesses
pixel_brightness = (red + green + blue) / 3
pixel_brightness2 = (red2 + green2 + blue2) / 3


# Get mean brightness
mean_brightness = (pixel_brightness + pixel_brightness2) / 2
print(mean_brightness)


