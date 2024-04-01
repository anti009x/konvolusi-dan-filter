import random
import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread('Data/simba.png', 0)
if citra is None:
    print('Berkas citra tak dapat dibaca')
else:
    filter = cv2.fastNlMeansDenoising(citra, None, 30)
    Hash = np.hstack((citra, filter))

# Tampilkan citra asal dan Hashnya
cv2.imshow('Hasil', Hash)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)