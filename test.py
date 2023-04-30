from image_gradient import *
import os 
def test():
    for file in os.listdir("Test_Images"):
        if file.endswith(".jpg"):
            im = Image.open("Test_Images/" + file)
            im = im.resize((300, 300 * im.size[1] // im.size[0]))
            gelb = getGELB(im)
            normalise(gelb)
            # fill_to_threshold(gelb, 150)
            get_cool_boy(im, gelb)
            im.save("Test_Images_Processed/cool/" + file)

            print(file)

if __name__ == "__main__":
    test()