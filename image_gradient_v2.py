import time
from PIL import Image
import math

def getGradient(im):
    width, height = im.size
    gradient = Image.new("L", (width, height))
    for x in range(width):
        for y in range(height):
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
            if pixel[0] > threshold or pixel[1] > threshold or pixel[2] > threshold:
                img.putpixel((x, y), (255, 255, 255))
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
    im = Image.open("Test_Images/test1.jpg")
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
    new_new_thing = fill_to_threshold(im, 100)
    im.show()
    im.save("Test_Images/tennisball1_gradient.jpg")