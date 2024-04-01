import random
import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread('Data/simbagdm.png', 0)
if citra is None:
    print('Berkas citra tak dapat dibaca')
else:
    terfilter = cv2.medianBlur(citra, 5)
    hasil = np.hstack((citra, terfilter))

# Tampilkan citra asal dan hasilnya
cv2.imshow('Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

