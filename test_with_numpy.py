from email.mime import image
from PIL import Image
import time
import os
import numpy as np
from timeit import timeit
def process():
    for image in os.listdir("Test_Images"):
        if not image.endswith(".jpg"):
            continue
        im = Image.open("Test_Images/" + image)
        image_array = np.array(im)
        height, width, colors = image_array.shape
        res = np.zeros((height, width), dtype=np.uint8)
        for x in range(width):
            for y in range(height):
                yellow = 255 - image_array[y, x, 0] + 255 - image_array[y, x, 1] + image_array[y, x, 2]
                yellow = 255 - yellow if yellow < 255 else 0
                res[y, x] = yellow
        im = Image.fromarray(res)
        im.save("Test_Images_Processed/" + image)

def check_for_tennisball(im: Image, yellow_threshold=200, counter_threshold=100):
    image_array = np.array(im)
    height, width, colors = image_array.shape
    counter = 0
    for x in range(int(1/3 * width), int(2/3 * width)):
        for y in range(height):
            yellow = 255 - image_array[y, x, 0] + 255 - image_array[y, x, 1] + image_array[y, x, 2]
            yellow = 255 - yellow if yellow < 255 else 0
            if yellow > yellow_threshold:
                counter += 1
        if counter > counter_threshold:
            return True
    return counter > counter_threshold

if __name__ == "__main__":
    start = time.time()
    counter = 0
    for image in os.listdir("Test_Images"):
        if not image.endswith(".jpg"):
            continue
        counter += 1
        im = Image.open("Test_Images/" + image)
        if check_for_tennisball(im, 100, 1):
            print(f"{image}: Tennisball")
        else:
            print(f"{image}: Not Tennisball")
    print(f"Finished {counter} images in {time.time() - start} seconds")