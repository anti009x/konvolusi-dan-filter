import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread('Data/goldhill.png', 0)
kernel = np.float32([[1, 1, 1],
[1, 1, 1],
[1, 1, 1]]) / 9
terfilter = cv2.filter2D(citra, -1, kernel)
combine = np.hstack((citra, terfilter))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Hasil', terfilter)
cv2.imshow("ori",citra)
cv2.imshow("Gabungan",combine)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)