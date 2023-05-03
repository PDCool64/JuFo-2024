import time
from PIL import Image

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

def fill_to_threshold(img, threshold):
    width, height = img.size
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            if pixel > threshold:
                img.putpixel((x, y), 255)
            else: img.putpixel((x, y), 0)

def tennisball(img, threshold):
    width, height = img.size
    counter = 0
    for x in range(width // 3, 2 * width // 3):
        for y in range(height):
            pixel = img.getpixel((x, y))
            if pixel > threshold:
                counter += 1
            else:
                pass
    if counter > 100:
        print("Tennisball")
    else:
        print("Kein Tennisball")
    print(counter)

if __name__ == "__main__":
    im = Image.open("Test_Images/test1.jpg")
    print(im.format, im.size, im.mode)
    im.draft(im.mode, (300, 300))
    calc_time = time.time()
    ylw = getGELB(im)
    tennisball(ylw, 80)
    print("Done calculating gradient after", time.time() - calc_time, "seconds")
    ylw.show()
