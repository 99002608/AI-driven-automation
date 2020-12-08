import numpy as np
import argparse
import imutils
import glob
import cv2
import pyautogui
def Avg(a,b):
    c=0
    sum=[]
    for i in range(len(a)):
        c=a[i]+b[i]
        c=int(c/2)
        sum.append(c)
    #sum[0]=sum[0]+439
    sum[1]=sum[1]+60
    print(sum)
    return sum


def cross():

        template = cv2.imread("D:\shadowML-main\pic\cross.png")
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        template = cv2.Canny(template, 50, 200)
        (tH, tW) = template.shape[:2]
        #cv2.imshow("Template", template)

        # loop over the images to find the template in
        for imagePath in glob.glob("D:\main" + "/*.png"):
                # load the image, convert it to grayscale, and initialize the
                # bookkeeping variable to keep track of the matched region
                image = cv2.imread(imagePath)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                found = None
                # loop over the scales of the image
                for scale in np.linspace(0.2, 1.0, 20)[::-1]:
                        # resize the image according to the scale, and keep track
                        # of the ratio of the resizing
                        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
                        r = gray.shape[1] / float(resized.shape[1])
                        # if the resized image is smaller than the template, then break
                        # from the loop
                        if resized.shape[0] < tH or resized.shape[1] < tW:
                                break
        # detect edges in the resized, grayscale image and apply template
                        # matching to find the template in the image
                        edged = cv2.Canny(resized, 50, 200)
                        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
                        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

                        if found is None or maxVal > found[0]:
                                found = (maxVal, maxLoc, r)

                (_, maxLoc, r) = found
                (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
                (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
                #cv2.imshow("Image", image)
                cv2.waitKey(0)
                X=(startX, startY)
                Y=(endX, endY)
                avg=Avg(X,Y)
        return avg



def cart():

        template = cv2.imread("D:\shadowML-main\pic\Cart.png")
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        template = cv2.Canny(template, 50, 200)
        (tH, tW) = template.shape[:2]
        #cv2.imshow("Template", template)

        # loop over the images to find the template in
        for imagePath in glob.glob("D:\main" + "/*.png"):
                # load the image, convert it to grayscale, and initialize the
                # bookkeeping variable to keep track of the matched region
                image = cv2.imread(imagePath)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                found = None
                # loop over the scales of the image
                for scale in np.linspace(0.2, 1.0, 20)[::-1]:
                        # resize the image according to the scale, and keep track
                        # of the ratio of the resizing
                        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
                        r = gray.shape[1] / float(resized.shape[1])
                        # if the resized image is smaller than the template, then break
                        # from the loop
                        if resized.shape[0] < tH or resized.shape[1] < tW:
                                break
        # detect edges in the resized, grayscale image and apply template
                        # matching to find the template in the image
                        edged = cv2.Canny(resized, 50, 200)
                        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
                        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

                        if found is None or maxVal > found[0]:
                                found = (maxVal, maxLoc, r)

                (_, maxLoc, r) = found
                (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
                (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
                #cv2.imshow("Image", image)
                cv2.waitKey(0)
                X=(startX, startY)
                Y=(endX, endY)
                avg=Avg(X,Y)
        return avg
def delivery():

        template = cv2.imread("D:\shadowML-main\pic\Delivery.png")
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        template = cv2.Canny(template, 50, 200)
        (tH, tW) = template.shape[:2]
        #cv2.imshow("Template", template)

        # loop over the images to find the template in
        for imagePath in glob.glob("D:\main" + "/*.png"):
                # load the image, convert it to grayscale, and initialize the
                # bookkeeping variable to keep track of the matched region
                image = cv2.imread(imagePath)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                found = None
                # loop over the scales of the image
                for scale in np.linspace(0.2, 1.0, 20)[::-1]:
                        # resize the image according to the scale, and keep track
                        # of the ratio of the resizing
                        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
                        r = gray.shape[1] / float(resized.shape[1])
                        # if the resized image is smaller than the template, then break
                        # from the loop
                        if resized.shape[0] < tH or resized.shape[1] < tW:
                                break
        # detect edges in the resized, grayscale image and apply template
                        # matching to find the template in the image
                        edged = cv2.Canny(resized, 50, 200)
                        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
                        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

                        if found is None or maxVal > found[0]:
                                found = (maxVal, maxLoc, r)

                (_, maxLoc, r) = found
                (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
                (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
                #cv2.imshow("Image", image)
                cv2.waitKey(0)
                X=(startX, startY)
                Y=(endX, endY)
                avg=Avg(X,Y)
        return avg
def options():

        template = cv2.imread("D:\shadowML-main\pic\Options.png")
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        template = cv2.Canny(template, 50, 200)
        (tH, tW) = template.shape[:2]
        #cv2.imshow("Template", template)

        # loop over the images to find the template in
        for imagePath in glob.glob("D:\main" + "/*.png"):
                # load the image, convert it to grayscale, and initialize the
                # bookkeeping variable to keep track of the matched region
                image = cv2.imread(imagePath)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                found = None
                # loop over the scales of the image
                for scale in np.linspace(0.2, 1.0, 20)[::-1]:
                        # resize the image according to the scale, and keep track
                        # of the ratio of the resizing
                        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
                        r = gray.shape[1] / float(resized.shape[1])
                        # if the resized image is smaller than the template, then break
                        # from the loop
                        if resized.shape[0] < tH or resized.shape[1] < tW:
                                break
        # detect edges in the resized, grayscale image and apply template
                        # matching to find the template in the image
                        edged = cv2.Canny(resized, 50, 200)
                        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
                        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

                        if found is None or maxVal > found[0]:
                                found = (maxVal, maxLoc, r)

                (_, maxLoc, r) = found
                (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
                (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
                #cv2.imshow("Image", image)
                cv2.waitKey(0)
                X=(startX, startY)
                Y=(endX, endY)
                avg=Avg(X,Y)
        return avg
def add():

        template = cv2.imread("D:\shadowML-main\pic\AddToBag.png")
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        template = cv2.Canny(template, 50, 200)
        (tH, tW) = template.shape[:2]
        #cv2.imshow("Template", template)

        # loop over the images to find the template in
        for imagePath in glob.glob("D:\main" + "/*.png"):
                # load the image, convert it to grayscale, and initialize the
                # bookkeeping variable to keep track of the matched region
                image = cv2.imread(imagePath)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                found = None
                # loop over the scales of the image
                for scale in np.linspace(0.2, 1.0, 20)[::-1]:
                        # resize the image according to the scale, and keep track
                        # of the ratio of the resizing
                        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
                        r = gray.shape[1] / float(resized.shape[1])
                        # if the resized image is smaller than the template, then break
                        # from the loop
                        if resized.shape[0] < tH or resized.shape[1] < tW:
                                break
        # detect edges in the resized, grayscale image and apply template
                        # matching to find the template in the image
                        edged = cv2.Canny(resized, 50, 200)
                        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
                        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

                        if found is None or maxVal > found[0]:
                                found = (maxVal, maxLoc, r)

                (_, maxLoc, r) = found
                (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
                (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
                #cv2.imshow("Image", image)
                cv2.waitKey(0)
                X=(startX, startY)
                Y=(endX, endY)
                avg=Avg(X,Y)
        return avg

def coordinates_click(a,b):
    pyautogui.click(a,b) 