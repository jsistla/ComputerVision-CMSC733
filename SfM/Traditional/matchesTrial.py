import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# MIN_MATCH_COUNT = 10s

# img1 = cv2.imread('box.png',0)          # queryImage
# img2 = cv2.imread('box_in_scene.png',0) # trainImage


import numpy as np
import cv2
import matplotlib.pyplot as plt

# img1 = cv2.imread('/home/shar/home.jpg',0)          # queryImage
# img2 = cv2.imread('/home/shar/home2.jpg',0) # trainImage
img1 = cv2.imread('Data/' + str(1) + '.jpg', 0)
img2 = cv2.imread('Data/' + str(2) + '.jpg', 0)


# Initiate SIFT detector
orb = cv2.ORB()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1, des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2)

plt.imshow(img3),plt.show()
