
import cv2
import numpy as np

img = cv2.imread("Stadium1.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#green range
g = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
ig = g>0
green = np.zeros_like(img, np.uint8)
green[ig] = img[ig]
cv2.imwrite("green.png", green)
greenImage = cv2.imread('green.png',0)

#make the output binary
def tresh(input):

    output = input.copy()
    output[input > 30] = 255
    output[input < 30] = 0

    return output


image = cv2.imread('green.png',0)
#cimg = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
img = tresh(image);
cv2.imwrite('stadiumoutout.png', img)
greenImage = cv2.imread('stadiumoutout.png',0)

#kernel for erode and dilate
kernel =cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
np.array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=np.uint8)



kernel2 =cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
np.array([[  1, 1],
       [ 1, 1]], dtype=np.uint8)

image = cv2.imread('green.png',0)
#binary image
img = tresh(image);


#erode and dilate a little so output is better!
erosion = cv2.erode(greenImage,kernel,iterations = 1)
erosion = cv2.erode(erosion,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
dilation = cv2.dilate(dilation,kernel,iterations = 1)
dilation = cv2.dilate(dilation,kernel,iterations = 1)



cv2.imshow('final',dilation)
cv2.waitKey(0)
cv2.imwrite('Stadium1output.jpg',erosion)
