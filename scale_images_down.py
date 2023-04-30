import os
from PIL import Image

def scale_down():
    for file in os.listdir("Test_Images_Original"):
        if file.endswith(".jpg"):
            im = Image.open("Test_Images_Original/" + file)
            im = im.resize((300, 300 * im.size[1] // im.size[0]))
            im.save("Test_Images/" + file)
            print(file) 



if __name__ == "__main__":
    scale_down()