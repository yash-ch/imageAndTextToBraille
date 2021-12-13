# Python script to convert the given image
# into a dotted text using opencv
  
# import the required modules
import cv2
from PIL import Image, ImageDraw, ImageFont
import os
import requests

from modifiedbraillegraph import vertical_graph, horizontal_graph

# Read the image
def imagetobraille(image_location = "", size =100, inverse = 0):
    
    if image_location == "":
        return "Image location not specified"

    img = cv2.imread(image_location, 0)

    # Apply median blur
    try:
        img = cv2.medianBlur(img, 5)
    except:
        return "Image location incorrect"
    
    # Apply MEAN thresholding to get refined edges
    image = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Preserve the ratio
    ratio = len(image)/len(image[0])
    # Assign new width and calculate new height
    new_height = size
    new_width = int(ratio*new_height)
    # Resize the image
    image = cv2.resize(image, (new_height, new_width))

    fillone = 0
    filltwo = 2

    if inverse == 1:
        fillone = 2
        filltwo = 0
    # Iterate over the array and print the dark pixels
    # or we can use any other symbol too.
    outputart = ""
    b=0

    pixellist1 = []
    pixellist2 = []
    pixellist3 = []
    pixellist4 = []

    noofdotslist1 = []
    noofdotslist2 = []
    noofdotslist3 = []
    noofdotslist4 = []

    # print(image[0])
    for i in range(len(image)):

        for j in range(len(image[0])):
            if b==0:
                if image[i, j] < 200:
                    pixellist1.append(0)
                else:
                    pixellist1.append(1)
            elif b==1:
                if image[i, j] < 200:
                    pixellist2.append(0)
                else:
                    pixellist2.append(1)
            elif b==2:
                if image[i, j] < 200:
                    pixellist3.append(0)
                else:
                    pixellist3.append(1)
            elif b==3:
                if image[i, j] < 200:
                    pixellist4.append(0)
                else:
                    pixellist4.append(1)

        if len(pixellist1)%2 !=0:
            pixellist1.append(1)
            pixellist2.append(1)
            pixellist3.append(1)
            pixellist4.append(1)

        b += 1
        
        if b==4:
            for k in range(0,len(pixellist1),2):
                
                if pixellist1[k] == 1 and pixellist1[k+1] == 1:
                    noofdotslist1.append(fillone)
                elif pixellist1[k] == 1 and pixellist1[k+1] == 0:
                    noofdotslist1.append(-1)
                elif pixellist1[k] == 0 and pixellist1[k+1] == 1:
                    noofdotslist1.append(1)
                else:
                    noofdotslist1.append(filltwo)

                if pixellist2[k] == 1 and pixellist2[k+1] == 1:
                    noofdotslist2.append(fillone)
                elif pixellist2[k] == 1 and pixellist2[k+1] == 0:
                    noofdotslist2.append(-1)
                elif pixellist2[k] == 0 and pixellist2[k+1] == 1:
                    noofdotslist2.append(1)
                else:
                    noofdotslist2.append(filltwo)

                if pixellist3[k] == 1 and pixellist3[k+1] == 1:
                    noofdotslist3.append(fillone)
                elif pixellist3[k] == 1 and pixellist3[k+1] == 0:
                    noofdotslist3.append(-1)
                elif pixellist3[k] == 0 and pixellist3[k+1] == 1:
                    noofdotslist3.append(1)
                else:
                    noofdotslist3.append(filltwo)

                if pixellist4[k] == 1 and pixellist4[k+1] == 1:
                    noofdotslist4.append(fillone)
                elif pixellist4[k] == 1 and pixellist4[k+1] == 0:
                    noofdotslist4.append(-1)
                elif pixellist4[k] == 0 and pixellist4[k+1] == 1:
                    noofdotslist4.append(1)
                else:
                    noofdotslist4.append(filltwo)

            try:
                for l in range(0,len(noofdotslist1)):
                    
                    if noofdotslist1[l] or noofdotslist2[l] or noofdotslist3[l] or noofdotslist4[l] != 0:
                        outputart += vertical_graph([noofdotslist1[l], noofdotslist2[l], noofdotslist3[l], noofdotslist4[l]])
                    else:    
                        outputart +=" "
            except:
                print("KYA HUA")

            outputart += "\n"  

            pixellist1.clear()
            pixellist2.clear()
            pixellist3.clear()
            pixellist4.clear()

            noofdotslist1.clear()
            noofdotslist2.clear()
            noofdotslist3.clear()
            noofdotslist4.clear()
            
            b=0

    # cv2.waitKey(0)
    return outputart

#download font file in .tff format
def texttobraille(font_location : str,text : str, size = 100, inverse = 0):
    image_url = "https://i.imgur.com/CykXjV9.jpg"    
    im = Image.open(requests.get(image_url, stream=True).raw)
    im.save("imagetobrailleartblankpic.jpg")

    textimg = Image.open('imagetobrailleartblankpic.jpg')
    d1 = ImageDraw.Draw(textimg)
    myFont = ImageFont.truetype(font_location, 100)
    d1.text((0, 0), text, fill =(0, 0, 0),font = myFont)

    textimg.save("{}.jpg".format(text))
    brailleart = imagetobraille(text+".jpg", size, inverse) 
    textimg.show()   
    os.remove("{}.jpg".format(text))
    os.remove("imagetobrailleartblankpic.jpg")
    return brailleart