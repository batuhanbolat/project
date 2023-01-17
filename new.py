#1
#https://www.codegrepper.com/code-examples/python/how+to+convert+grayscale+image+to+binary+image+in+opencv
import cv2
originalImage=cv2.imread(r'C:\Users\340\Desktop/bird.jpg')# read the image
grayImage=cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage) 
cv2.waitKey(0)#prevents the code from being interrupted
cv2.destroyAllWindows()#close the window
#2
#https://www.youtube.com/watch?v=77Rj12AXNho
import numpy as np
x = np.random.randint(100,size=(10,10))#write random number and create 10 row and 10 colomn
print (x)
