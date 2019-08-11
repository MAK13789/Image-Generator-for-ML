import random
import os
import numpy as np
import cv2
def noise(image, temp):
    output = np.zeros(image.shape,np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            output[i][j] = image[i][j] + random.randint(-temp, temp)
    return output
def rotate(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result
image = cv2.imread('Dog.png')
path = 'C:/Users/Ahsan/Desktop/more dog images'
#GENERATE MORE IMAGES FOR BETTER TRAINING, AND IF THAT DOESN't WORK USE 10 LEGIT IMAGES FOR TRAINING INSTEAD OF1
for k in range(300, 1000):
    temp = random.randint(0, 100)
    angle = random.randint(0, 360)
    new_img = noise(image, temp)
    final_img = rotate(new_img, angle)
    name = str(k) + '.jpg'
    cv2.imwrite(os.path.join(path, name), final_img)

