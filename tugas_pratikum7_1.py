import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread('Data/logo_polindra_noise.png', 0)

# citra = cv2.resize(citra, (312, 312))

if citra is None:
    print('Berkas citra tak dapat dibaca')
else:
    terfilter = cv2.medianBlur(citra, 7)
    # hasil = np.hstack((citra, terfilter))


# Tampilkan citra awal dan hasilnya
cv2.imshow('Gambar_Asli', citra)
cv2.imshow('Hasil', terfilter)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

