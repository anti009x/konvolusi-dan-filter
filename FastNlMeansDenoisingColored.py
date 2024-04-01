import random
import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread('Data/simba.png')
if citra is None:
    print('Berkas citra tak dapat dibaca')
else:
    terfilter = cv2.fastNlMeansDenoisingColored(citra, None, 30, 30)
    hash = np.hstack((citra, terfilter))
# Tampilkan citra asal dan hashnya
cv2.imshow('Hasil', hash)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)