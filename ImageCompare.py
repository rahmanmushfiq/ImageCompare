import cv2
import numpy as np
import os

imagePath = os.getcwd()+"/Images/"
image0 = cv2.imread(imagePath+"0.png")
image1 = cv2.imread(imagePath+"1.png")
difference = cv2.subtract(image0, image1)
result = np.any(difference)

if result:
    print("The images are different...")
    cv2.imwrite(imagePath+"Result.jpg", difference)
else:
    print("There is no Difference between images...")