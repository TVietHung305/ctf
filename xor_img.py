import cv2

img1 = cv2.imread('D:\Downloads\pic1.png')
img2 = cv2.imread('D:\Downloads\pic2.png')

final_xor = cv2.bitwise_xor(img1,img2,mask=None)
cv2.imshow('Xor', final_xor)
cv2.waitKey(0)

