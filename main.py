#!/usr/local/bin/python3

import base64, sys, os.path
sys.path.append('/usr/local/python3.5/site-packages')
import cv2 as cv
from LSBSteg import LSBSteg


#Hide text
def hide_text(text, in_img, out_img="res.png"):
    carrier = cv.imread(in_img)
    steg = LSBSteg(carrier)
    if (os.path.isfile(text)):
        f = open(text,'r')
        text = f.read()

    steg.hideText(text)
    steg.saveImage(out_img)

#Unhide text
def unhide_text(in_img):
    im = cv.imread(in_img)
    steg = LSBSteg(im)
    print(steg.unhideText())

#Hide image
def hide_image(secret_img, carrier_img, out_img="res.png"):
    imagetohide = cv.LoadImage(secret_img)
    carrier = cv.LoadImage(carrier_img)
    steg = LSBSteg(carrier)
    steg.hideImage(imagetohide)
    steg.saveImage(out_img)

#Unhide image
def unhide_image(in_img,out_img):
    inp = cv.LoadImage(in_img)
    steg = LSBSteg(inp)
    dec = steg.unhideImage()
    cv.SaveImage(out_img, dec) #Image retrieve into the other image


#Hide binary
def hide_binary(in_img, out_img):
    carrier = cv.LoadImage(in_img)
    steg = LSBSteg(carrier)
    steg.hideBin("ls") #I took the first binary I found
    steg.saveImage(out_img)

#Unhide binary
def unhide_binary(in_img):
    inp = cv.LoadImage("res.png")
    steg = LSBSteg(inp)
    bin = steg.unhideBin()
    f = open("res","wb") #Write the binary back to a file
    f.write(bin)
    f.close()

def helper():
    example1 = """* to hide text *\nexample: python3 main.py hide_text \"hello world\" original.png out.png"""
    example2 = """* to unhide text *\nexample: python3 main.py unhide_text out.png"""
    example3 = """* other options *\nhide_image, unhide_image, hide_binary, unhide_binary"""
    print("\n\n||| WELCOME TO LSB STEG ||| \n\n%s\n\n%s\n\n%s\n\nENJOY\n\n" % (example1,example2,example3))
    sys.exit()

if __name__=="__main__":
    if len(sys.argv) < 2:
        raise Exception("Arguments must be at least 1!")
    else:
        first = sys.argv[1]
        if first == "hide_text":
            hide_text(sys.argv[2],sys.argv[3],sys.argv[4])
        elif first == "unhide_text":
            unhide_text(sys.argv[2])
        elif first == "hide_image":
            hide_image(sys.argv[2],sys.argv[3],sys.argv[4])
        elif first == "unhide_image":
            unhide_image(sys.argv[2],sys.argv[3])
        elif first == "hide_binary":
            hide_binary(sys.argv[2],sys.argv[3])
        elif first == "unhide_binary":
            unhide_binary(sys.argv[2])
        elif first == "-h":
            helper()
        else:
            raise Exception(first+" was a not valid argument! run -h for help")

