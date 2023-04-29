import time
from PIL import Image
import math

def getGradient(im):
    width, height = im.size
    gradient = Image.new("L", (width, height))
    for x in range(width):
        for y in range(height):
    #         pixel = im.getpixel((x, y))
    #         if y == 0:
    #             pixel_above = pixel
    #         else:
    #             pixel_above = im.getpixel((x, y-1))
    #         if y == height - 1:
    #             pixel_below = pixel
    #         else:
    #             pixel_below = im.getpixel((x, y+1))
    #         if x == 0:
    #             pixel_left = pixel
    #         else:
    #             pixel_left = im.getpixel((x-1, y))
    #         if x == width - 1:
    #             pixel_right = pixel
    #         else:
    #             pixel_right = im.getpixel((x+1, y))

    #         diff_y = 0
    #         if y > 0:
    #             diff_y += sum([abs(pixel[i] - pixel_above[i]) for i in range(3)])
    #         if y < height - 1:
    #             diff_y += sum([abs(pixel[i] - pixel_below[i]) for i in range(3)])
    #         diff_x = 0
    #         if x > 0:
    #             diff_x += sum([abs(pixel[i] - pixel_left[i]) for i in range(3)])
    #         if x < width - 1:
    #             diff_x += sum([abs(pixel[i] - pixel_right[i]) for i in range(3)])
    #         diff = diff_x + diff_y
            gradient.putpixel((x, y), 255 - (get_difference_from_surounding_pixels(im, x, y, 1)//2))

    return gradient

def get_difference_from_surounding_pixels(image, x, y, radius=1):
    width, height = image.size
    pixel = image.getpixel((x, y))
    pixels = []
    difference = 0
    pixel_to_compare = {(x, y-1), (x, y+1), (x-1, y), (x+1, y)}
    for x, y in pixel_to_compare:
        if 0 <= x < width and 0 <= y < height:
            pixels.append(image.getpixel((x, y)))
    
    for pix in pixels:
        difference += sum([abs(pixel[i] - pix[i]) for i in range(3)])
    return difference


def getGELB(image):
    result = Image.new("L", image.size)
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            error = 255 - pixel[0] + 255 - pixel[1] + pixel[2]
            error = 255 - error if error < 255 else 0
            result.putpixel((x, y), error)
    return result

def subtract_per_pixel(image1, image2):
    width, height = image1.size
    result = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))
            result.putpixel((x, y), tuple([abs(pixel1[i] - pixel2[i]) for i in range(3)]))
    return result

def multiply_per_pixel(image1, image2):
    width, height = image1.size
    result = Image.new("L", (width, height))
    for x in range(width):
        for y in range(height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))
            result.putpixel((x, y), pixel1 * pixel2 // 255)
    return result

def fill_to_threshold(img, threshold):
    visited = set()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            if pixel > threshold:
                img.putpixel((x, y), 255)
            else: img.putpixel((x, y), 0)
    
        
def find_objects_of_size(img, size):
    visited = set()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            if pixel:
                pass
            
            
def get_cool_boy(original, mask):
    width, height = original.size
    for x in range(width):
        for y in range(height):
            pixel = original.getpixel((x, y))
            r = pixel[0] * (0.2 + mask.getpixel((x, y)) / 310)
            g = pixel[1] * (0.2 + mask.getpixel((x, y)) / 310)
            b = pixel[2] * (0.2 + mask.getpixel((x, y)) / 310)
            original.putpixel((x, y), (int(r), int(g), int(b)))

if __name__ == "__main__":
    im = Image.open("Test_Images/test3.jpg")
    print(im.format, im.size, im.mode)
    im.draft(im.mode, (300, 300))
    tim = time.time()
    JELP = getGELB(im)
    print("Done calculating gradient after", time.time() - tim, "seconds")
    JELP.show()
    gradient = getGradient(im)
    gradient.show()
    new_new_thing = multiply_per_pixel(JELP, gradient)
    new_new_thing.show()
    get_cool_boy(im, new_new_thing)
    im.show()