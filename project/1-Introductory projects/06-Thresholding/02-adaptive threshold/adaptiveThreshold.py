import cv2

img = cv2.imread('sudoku.png', 0)

#adaptiveThreshold is used to apply the thresholding
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)

cv2.imshow('image', img)

cv2.imshow('thresh1', th1)
cv2.imshow('thresh2', th2)

cv2.waitKey(0)
cv2.destroyAllWindows()

