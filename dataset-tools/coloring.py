import cv2 as cv
import numpy as np

img = cv.imread(
    '/Users/khaledkaddal/Desktop/resense/Gearloose/DataSets/Nila/1_input/NilaajmId_420.jpeg'
)

###############
# Color Spaces
###############

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.startWindowThread()

hsv2BGR = cv.cvtColor(img, cv.COLOR_HSV2BGR)
lab2BGR = cv.cvtColor(img, cv.COLOR_LAB2BGR)
rgb2BGR = cv.cvtColor(img, cv.COLOR_RGB2BGR)

cv.imwrite('subject-main.jpg', img)
cv.imwrite('subject-gray.jpg', gray)
cv.imwrite('subject-hsv.jpg', hsv)
cv.imwrite('subject-lab.jpg', lab)
cv.imwrite('subject-rgb.jpg', rgb)

cv.imwrite('subject-hsv2BGR.jpg', hsv2BGR)
cv.imwrite('subject-lab2BGR.jpg', lab2BGR)
cv.imwrite('subject-rgb2BGR.jpg', rgb2BGR)

##################
# Color Channels
##################

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imwrite('subject-blue.jpg', blue)
cv.imwrite('subject-green.jpg', green)
cv.imwrite('subject-red.jpg', red)

cv.waitKey(1)
cv.destroyAllWindows()
cv.waitKey(1)

# from __future__ import print_function
# from builtins import input
# import cv2 as cv
# import numpy as np
# import argparse
# # Read image given by user

# image = cv.imread('18.jpg')

# if image is None:
#     print('Could not open or find the image: ', args.input)
#     exit(0)
# new_image = np.zeros(image.shape, image.dtype)
# alpha = 1.0 # Simple contrast control
# beta = 0    # Simple brightness control
# # Initialize values
# print(' Basic Linear Transforms ')
# print('-------------------------')
# try:
#     alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
#     beta = int(input('* Enter the beta value [0-100]: '))
# except ValueError:
#     print('Error, not a number')
# # Do the operation new_image(i,j) = alpha*image(i,j) + beta
# # Instead of these 'for' loops we could have used simply:
# new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
# # but we wanted to show you how to access the pixels :)
# # for y in range(image.shape[0]):
# #     for x in range(image.shape[1]):
# #         for c in range(image.shape[2]):
# #             new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
# cv.imwrite('OriginalImage.jpg', image)
# cv.imwrite('NewImage.jpg', new_image)
# # Wait until user press some key
# cv.waitKey(1)
# cv.destroyAllWindows()
# cv.waitKey(1)