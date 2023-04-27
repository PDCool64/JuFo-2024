from PIL import Image
import math
im = Image.open("tennisball2.jpg")
print(im.format, im.size, im.mode)
### Get the gradient of the image
def getGradient(im):
    # Get the size of the image
    width, height = im.size
    # Create a new image of the same size
    gradient = Image.new("L", (width, height))
    # For every pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the pixel value
            pixel = im.getpixel((x, y))
            if y == 0:
                pixel_above = pixel
            else:
                pixel_above = im.getpixel((x, y-1))
            if y == height - 1:
                pixel_below = pixel
            else:
                pixel_below = im.getpixel((x, y+1))
            if x == 0:
                pixel_left = pixel
            else:
                pixel_left = im.getpixel((x-1, y))
            if x == width - 1:
                pixel_right = pixel
            else:
                pixel_right = im.getpixel((x+1, y))

            ### Calculate the difference between the pixel and the pixels around it
            # Calculate the difference between the pixel and the pixel above
            diff_y = 0
            if y > 0:
                diff_y += sum([abs(pixel[i] - pixel_above[i]) for i in range(3)])
            # Calculate the difference between the pixel and the pixel below
            if y < height - 1:
                diff_y += sum([abs(pixel[i] - pixel_below[i]) for i in range(3)])
            # Calculate the difference between the pixel and the pixel to the left
            diff_x = 0
            if x > 0:
                diff_x += sum([abs(pixel[i] - pixel_left[i]) for i in range(3)])
            # Calculate the difference between the pixel and the pixel to the right
            if x < width - 1:
                diff_x += sum([abs(pixel[i] - pixel_right[i]) for i in range(3)])
            # The total difference is the sum of the differences in x and y
            diff = diff_x + diff_y
            # Insert the gradient into the image
            gradient.putpixel((x, y), diff//2)

    return gradient
gradient = getGradient(im)
gradient.show()