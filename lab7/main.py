import numpy as np
import cv2
from matplotlib import pyplot as plt

def findTheGhost(img1, img2):
    """
           Функция позволяющая находить и выделять ИЗВЕСТНЫЕ
           объекты на каком-либо фоне.

           Parameters
           ----------
           img1: image
              a template (ghost)
           img2: image
              original image

           Returns
           -------
           img3 : image
               Картинка, на фон оригинала наложен белый квадрат, выделяюзий призрака:

    """
    # set a condition that at least 10 matches are to be there to find the object
    MIN_MATCH_COUNT = 10

    # Initiate SIFT detector
    sift = cv2.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)

    # store all the good matches as per Lowe's ratio test.
    goodMatch = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            goodMatch.append(m)

    if len(goodMatch) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in goodMatch]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in goodMatch]).reshape(-1, 1, 2)
        # we pass the set of points from both the images, cv2.findHomography will find the perspective transformation
        # of that object.
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        h, w = img1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        # use cv2.perspectiveTransform() to find the object.
        # It needs at least four correct points to find the transformation.
        dst = cv2.perspectiveTransform(pts, M)

        img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                       singlePointColor=None,
                       matchesMask=matchesMask,  # draw only inliers
                       flags=2)

    img3 = cv2.drawMatches(img1, kp1, img2, kp2, goodMatch, None, **draw_params)

    plt.imshow(img3, 'gray'), plt.show()


def main():

    img1 = cv2.imread('candy_ghost.png', 0)
    img2 = cv2.imread('lab7.png', 0)
    findTheGhost(img1, img2)
    img1 = cv2.imread('pampkin_ghost.png', 0)
    findTheGhost(img1, img2)
    img1 = cv2.imread('scary_ghost.png', 0)
    findTheGhost(img1, img2)

if __name__ == '__main__':
    main()
