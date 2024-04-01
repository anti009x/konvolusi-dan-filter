import random
import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread('Data/simba.png', 0)
hasil = citra.copy()  # Salin isi citra
jumBaris, jumKolom = hasil.shape
prob = 0.1
for baris in range(jumBaris):
    for kolom in range(jumKolom):
        nilaiAcak = random.random()
        if nilaiAcak < prob / 2:
            hasil[baris, kolom] = 0  # merica
        elif nilaiAcak <= prob:
            hasil[baris, kolom] = 255  # Garam
cv2.imshow('Original', citra)
cv2.imshow('Hasil Noise', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
# Simpan citra
cv2.imwrite('Data/simbagdm.png', hasil)
