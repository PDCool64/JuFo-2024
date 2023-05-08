from PIL import Image
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


print(timeit(process, number=1))