
import cv2
import numpy as np

img = cv2.imread("Stadium2.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#green range
g = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
ig = g>0
green = np.zeros_like(img, np.uint8)
green[ig] = img[ig]
cv2.imwrite("green2.png", green)
greenImage = cv2.imread('green2.png',0)

#make the output binary
def tresh(input):

    output = input.copy()
    output[input > 1] = 255
    output[input < 1] = 0

    return output


#kernel for erosion
kernel =cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
np.array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=np.uint8)


image = cv2.imread('green2.png',0)
#cimg = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
img = tresh(image);
cv2.imwrite('stadiumoutout2.png', img)
greenImage = cv2.imread('stadiumoutout2.png',0)

#erode a little so output is better!
erosion = cv2.erode(greenImage,kernel,iterations = 1)
erosion = cv2.erode(erosion,kernel,iterations = 1)
erosion = cv2.erode(erosion,kernel,iterations = 1)
erosion = cv2.erode(erosion,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
dilation = cv2.dilate(dilation,kernel,iterations = 1)

output = dilation

cv2.imshow('final',output)
cv2.waitKey(0)
cv2.imwrite('output.jpg',erosion)
