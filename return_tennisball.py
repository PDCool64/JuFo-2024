from PIL import Image

im = Image.open("Test_Images/tennisball1_gradient.jpg")

width, height = im.size

def test(im):
    for x in range(int(1/3 * width), int(2/3 * width)):
        for y in range(height):
            im.putpixel((x, y), (255, 255, 255))
    im.show()


def is_tennisball(im: Image):
    width, height = im.size
    for x in range(int(1/3 * width), int(2/3 * height)):
        for y in range(height):
            pixel = im.getpixel((x, y))
            if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
                return True





if __name__ == "__main__":
    if is_tennisball(im):
        print("Tennisball")
    else:
        print("Not Tennisball")
