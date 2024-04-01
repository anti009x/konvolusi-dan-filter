import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread('Data/simba.png')
blur1 = cv2.bilateralFilter(citra, 10, 75, 75)
blur2 = cv2.bilateralFilter(citra, 10, 150, 150)
hasil = np.hstack((citra, blur1, blur2))
# Tampilkan citra asal dan hasilnya
cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)