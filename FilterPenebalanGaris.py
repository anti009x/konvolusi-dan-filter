import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread('Data/lena.png', 0 )
kernel = np.float32([[0, 0, 0],
[ 4, 0, -4],
[ 0, 0, 0]])
terfilter = cv2.filter2D(citra, -1, kernel)
hasil = np.hstack((citra, terfilter))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)