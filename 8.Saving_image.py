import cv2
import  numpy as np

img=cv2.imread("Images/frt.jpg")
new_img=img[0:200,0:300]

cv2.imwrite("fruits_small.png",new_img) #Saving image using imwrite func

cv2.imshow("Crop_image",new_img)
cv2.waitKey(0)

ab=456
print(ab)