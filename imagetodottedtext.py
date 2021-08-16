# Python script to convert the given image
# into a dotted text using opencv
  
# import the required modules
import cv2
from braillegraph import vertical_graph, horizontal_graph
from PIL import Image, ImageDraw, ImageFont
import os

# Read the image
def brailletoart(image_name = "face2", size =100, inverse = "n", pngorjpg = "j" ):
    
    if pngorjpg == "j":
            image_name = "images\\"+ image_name + ".jpg"
    elif pngorjpg == "p":
            image_name = "images\\"+ image_name + ".png"         

    img = cv2.imread(image_name, 0)

    # Apply median blur
    img = cv2.medianBlur(img, 5)
    
    # Apply MEAN thresholding to get refined edges
    image = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # cv2.imshow("image", image)
    
    # Preserve the ratio
    ratio = len(image)/len(image[0])
    # Assign new width and calculate new height
    new_height = size
    new_width = int(ratio*new_height)
    # print(f"{new_width} {new_height}")
    # Resize the image
    image = cv2.resize(image, (new_height, new_width))

    fillone = 0
    filltwo = 2

    if inverse == "y":
        fillone = 2
        filltwo = 0
    # Iterate over the array and print the dark pixels
    # or we can use any other symbol too.
    a = ""
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
            # a += "   " if image[i, j] < 200 else ".  "
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
                        a += vertical_graph([noofdotslist1[l], noofdotslist2[l], noofdotslist3[l], noofdotslist4[l]])
                    else:    
                        a +=" "
            except:
                print("KYA HUA")

            a += "\n"  

            pixellist1.clear()
            pixellist2.clear()
            pixellist3.clear()
            pixellist4.clear()

            noofdotslist1.clear()
            noofdotslist2.clear()
            noofdotslist3.clear()
            noofdotslist4.clear()
            
            b=0


    print("\n"*5)
    print(a)
    # outputimg
    print("Done")
    cv2.waitKey(0)

def textedimage(text : str):
    textimg = Image.open('images/back.jpg')
    d1 = ImageDraw.Draw(textimg)
    myFont = ImageFont.truetype("font.ttf", 100)
    d1.text((5, 5), text.upper(), fill =(0, 0, 0), font= myFont)

    textimg.save("images\\{}.jpg".format(text))


while True:
    try:
        command = input("Enter command (t if text none if not text, image/text name, size, y for inverse and y for non inverse, j for jpg and p for png,): ")
        commandlist = command.split()

        if commandlist[0] == "t":
            
            texttoprint = ""
            for text in range(1,len(commandlist)-2):
                texttoprint = texttoprint + "{} ".format(commandlist[text])
            
            texttoprint = texttoprint[:-1]

            textedimage(texttoprint)

            brailletoart(texttoprint, int(commandlist[-2]), commandlist[-1])    
            os.remove("images\\{}.jpg".format(texttoprint))
        else:
            brailletoart(commandlist[0], commandlist[1], int(commandlist[2]), commandlist[3])    

    except BaseException as error:
        print('An exception occurred: {}'.format(error))
        continue
