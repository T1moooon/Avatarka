from PIL import Image
# import image
image_start = Image.open('monro.jpg')
image_start.convert('RGB')
red, green, blue = image_start.split()
# edit red
coordinates_red_left = (50, 0, red.width, red.height)
red_left = red.crop(coordinates_red_left)
coordinates_red_middle = (25, 0, red.width - 25, red.height)
red_middle = red.crop(coordinates_red_middle)
red_complete = Image.blend(red_middle, red_left, 0.7)
# edit green
coordinates_green = (25, 0, green.width - 25, green.height)
green_complete = green.crop(coordinates_green)
# edit blue
coordinates_blue_right = (0, 0, blue.width - 50, blue.height)
blue_right = blue.crop(coordinates_blue_right)
coordinates_blue_middle = (25, 0, blue.width - 25, blue.height)
blue_middle = blue.crop(coordinates_blue_middle)
blue_complete = Image.blend(blue_middle, blue_right, 0.7)
# Complete
new_image = Image.merge('RGB', (red_complete, green_complete, blue_complete))
new_image.save('monro_complete.jpg')
new_image.thumbnail((80, 80))
new_image.save('avatar.jpg')